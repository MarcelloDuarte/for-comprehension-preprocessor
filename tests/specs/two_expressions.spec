--DESCRIPTION--

Test two expressions

--GIVEN--

for {
    $a <- Some(42)
    $b <- Some($a + 1)
} yield $b;

--EXPECT--

Some(42)->flatMap(function ($a) {
    return Some($a + 1)->map(function ($b) use ($a) {
        return $b;
    });
});