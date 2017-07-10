--DESCRIPTION--

Test wildcard

--GIVEN--

for {
    ($a, $b) <- Some(Pair(1,2))
} yield $b;

--EXPECT--

Some(Pair(1, 2))->map(function ($tuple) {
    $a = $tuple->_1;
    $b = $tuple->_2;
    return $b;
});