--DESCRIPTION--

Test bind to tuples

--GIVEN--

for {
    ($a) <- Some(Tuple(1))
} yield $a;

for {
    ($a, $b) <- Some(Pair(1,2))
} yield $b;

for {
    ($a, $b, $c) <- Some(Tuple(1,2,3))
} yield ($a, $c);

--EXPECT--

Some(Tuple(1))->map(function ($tuple) {
    $a = $tuple->_1;
    return $a;
});

Some(Pair(1, 2))->map(function ($tuple) {
    $a = $tuple->_1;
    $b = $tuple->_2;
    return $b;
});

Some(Tuple(1, 2, 3))->map(function ($tuple) {
    $a = $tuple->_1;
    $b = $tuple->_2;
    $c = $tuple->_3;
    return Pair($a, $c);
});