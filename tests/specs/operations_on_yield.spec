--DESCRIPTION--

Test operations on yield

--GIVEN--

for {
    $a <- Some(42)
    $b <- Some(43)
} yield $a + $b - $a < $b && $a || $b ^ $a ?? $b > $a . $a <=> $b == $b >= $a != $a;

for {
    $a <- Some(42)
    $b <- Some(43)
} yield ($a + $b, $a - $b);

--EXPECT--

Some(42)->flatMap(function($a) {
    return Some(43)->map(function($b) use ($a) {
        return $a + $b - $a < $b && $a || $b ^ $a ?? $b > $a . $a <=> $b == $b >= $a != $a;
    });
});

Some(42)->flatMap(function($a) {
    return Some(43)->map(function($b) use ($a) {
        return Pair($a + $b, $a - $b);
    });
});