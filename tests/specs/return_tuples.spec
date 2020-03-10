--DESCRIPTION--

Test returning tuples

--GIVEN--

for {
    $a <- Some(42)
} yield ();

for {
    $a <- Some(42)
} yield ($a);

for {
    $a <- Some(42)
    $b <- Some(43)
} yield ($a, $b);

for {
    $a <- Some(42)
    $b <- Some(43)
    $c <- Some(44)
} yield ($a, $c, $b);

--EXPECT--

Some(42)->map(function($a) {
    return Unit();
});

Some(42)->map(function($a) {
    return Tuple($a);
});

Some(42)->flatMap(function($a) {
    return Some(43)->map(function($b) use ($a) {
        return Pair($a, $b);
    });
});

Some(42)->flatMap(function($a) {
    return Some(43)->flatMap(function($b) use ($a) {
        return Some(44)->map(function($c) use ($a, $b) {
            return Tuple($a, $c, $b);
        });
    });
});