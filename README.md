A for-comprenhensions pre-processor for PHP
===========================================

For-comprenhensions are syntax sugar for composing certain group of operations that can be found in monadic collections: `withEach`, `withFilter`, `filter`, `map` and `flatMap`. This pre-processor will translate the operations using the for-comprenhension syntax into pure PHP. This does not happen at runtime, so there is no hit on perfomance. The pre-processor works on top of the [pre](https://github.com/preprocess/pre-plugin) plugin and the [yay macro library](https://github.com/marcioAlmada/yay). 

Let's see how it works in practice with iteration, filtering, mapping and flatmapping.

Iteration
---------

```php
for ($a <- ImmList(1, 2, 3)) { echo $a; }
```

gets translated to:

```php
ImmList(1, 2, 3)->withEach(function ($a) {
    echo $a;
});
```

which prints

```
123
```

Ok, that's boring. PHP foreach does the same. Or does it? With this syntax you can do many iterations in one go.

```php
for ($a <- ImmList(1, 2, 3); $b <- ImmList($a); $c <- ImmList($b)) { echo $a + $b + $c; }
```

which translates to:
```php
ImmList(1, 2, 3)->withEach(function($a) {
    ImmList($a)->withEach(function($b) use ($a) {
        ImmList($b)->withEach(function($c) use ($a, $b) {
            echo ($a + $b + $c) . "\n";
        });
    });
});
```

and prints

```
3
6
9
```

Hmm! Starting to be interesting, huh? Oh! but's this is really nothing yet.

Mapping
-------

When using the `yield` keyword, one-liner for-comprehensions translate to mapping:

```php
for ($a <- ImmList(1, 2, 3)) yield $a + 1;
```

this becomes:

```php
ImmList(1, 2, 3)->map(function() {
    return $a + 1;
});
```

which produces a `ImmList(2, 3, 4)`.

Flatmapping
-----------

You can compose these expressions to create bigger expressions. When you add lines to your for-comprehension you get them translated into `flatMap` operations, only the last one remains a `map`.

```php
for {
    $a <- Some(42)
    $b <- Some($a + 1)
    $c <- Some($b + $a + 3)
} yield $c;
```

which gets translated into:

```php
Some(42)->flatMap(function ($a) {
    return Some($a + 1)->flatMap(function ($b) use ($a) {
        return Some($b + $a + 3)->map(function ($c) use ($a, $b) {
            return $c;
        });
    });
});
```

This is actually a very common pattern in functional programming and a very good way to keep operations within a pure context. The code below has no side effects and describes IO operations in a functional program.

```php
for {
    $line <- IO\readline()
    _ <- IO\write($line, '/tmp/some_file.txt')
    _ <- IO\printLn("You have successfully written to file")
} yield ()
```

Notice that you can use the wildcard `_` to ignore the return values of operations. The yield `()` will return a `IO<Unit>`. A unit is an empty product. If you are new to this, just think of it as a `void`. It's not, but that would do for now.

Filtering
---------

As we add operations to the for comprenhension we can add filters that will operate on the result of such operations, limiting what's given to the next operation.

```php
for {
    $a <- ImmList(1, 2, 3) if $a % 2 == 0
} yield $a;
```

this code is translated into:

```php
ImmList(1, 2, 3)->withFilter(function ($a) {
    return $a % 2 == 0;
})->map(function ($a) {
    return $a;
});
```

The result is a new List with only the elements that satisfy the predicate `$a % 2 == 0` or, in order words, are even.

A more complex example

```php
for {
    $a <- ImmList(1, 2, 3) if $a % 2 == 0
    $b <- ImmList(1, 2, 3) if $b % 2 != 0
} yield ($a, $b);
```

which translate to:

```php
ImmList(1, 2, 3)->withFilter(function ($a) {
    return $a % 2 == 0;
})->flatMap(function ($a) {
    return ImmList(1, 2, 3)->withFilter(function ($b) use ($a) {
        return $b % 2 != 0;
    })->map(function ($b) use ($a) {
        return Pair($a, $b);
    });
});
```

We can also add the filters in the next line:

```php
for {
    $a <- ImmList(1, 2, 3)
    $b <- ImmList(1, 2, 3)
    if $b % 2 != 0
} yield ($a, $b);

```

Which is the equivalent of having the filter next to the previous line.

```php
ImmList(1, 2, 3)->flatMap(function ($a) {
    return ImmList(1, 2, 3)->withFilter(function ($b) use ($a) {
        return $b % 2 != 0;
    })->map(function ($b) use ($a) {
        return Pair($a, $b);
    });
});
```

Note that the pre-processor recognises tuples syntax, so you can return tuples and have them assigned to more than one varible:

```php
for {
    ($a) <- Some(Tuple(1))
    ($b, $c) <- Some(Pair(1, 2))
} yield $b;
```

which translate to:

```php
Some(Tuple(1))->flatMap(function ($t2) {
    $a = $t2->_1;
    return Some(Pair(1, 2))->map(function ($t1) use ($a) {
        $b = $t1->_1;
        $c = $t1->_2;
        return $b;
    });
});
```

or you can return tuples:

```php
for {
    $a <- Some(42)
    $b <- Some(43)
} yield ($a, $b);
```

which maps to `Some(Pair(42,43))`.

Final Notes
-----------
 - This pre-processor is alpha software. Do not use it in production.
 - You don't need to use a library like Phunkie to use this pre-processor, but you will need to provide with Tuples and an interface for your monadic collections implementing `withEach`, `withFilter`, `filter`, `map` and `flatMap`.