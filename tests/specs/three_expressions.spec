--DESCRIPTION--

Test three expressions

--GIVEN--

for {
    $a <- Some(42)
    $b <- Some($a + 1)
    $c <- Some($b + $a + 3)
} yield $c;

--EXPECT--

Some(42)->flatMap(function($a) {
    return Some($a + 1)->flatMap(function($b) use ($a) {
        return Some($b + $a + 3)->map(function($c) use ($a, $b) {
            return $c;
        });
    });
});