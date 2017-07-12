--DESCRIPTION--

Test comprehension with condition

--GIVEN--

for ($a <- ImmList(1, 2, 3)) yield $a;

for ($a <- ImmList(1, 2, 3) if $a % 2 == 0 ) yield $a;

for {
    $a <- ImmList(1, 2, 3) if $a % 2 == 0
} yield $a;

for {
    $a <- ImmList(1, 2, 3) if $a % 2 == 0
    $b <- ImmList(1, 2, 3) if $b % 2 != 0
} yield ($a, $b);

--EXPECT--

ImmList(1, 2, 3)->map(function ($a) {
    return $a;
});

ImmList(1, 2, 3)->withFilter(function ($a) {
    return $a % 2 == 0;
})->map(function ($a) {
    return $a;
});

ImmList(1, 2, 3)->withFilter(function ($a) {
    return $a % 2 == 0;
})->map(function ($a) {
    return $a;
});

ImmList(1, 2, 3)->withFilter(function ($a) {
    return $a % 2 == 0;
})->flatMap(function ($a) {
    return ImmList(1, 2, 3)->withFilter(function ($b) use ($a) {
        return $b % 2 != 0;
    })->map(function ($b) use ($a) {
        return Pair($a, $b);
    });
});