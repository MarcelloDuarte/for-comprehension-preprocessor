--DESCRIPTION--

Test bind to tuples, multiple lines

--GIVEN--

for {
    ($a) <- Some(Tuple(1))
    ($b, $c) <- Some(Pair(1, 2))
} yield $b;

--EXPECT--

Some(Tuple(1))->flatMap(function ($t2) {
    $a = $t2->_1;
    return Some(Pair(1, 2))->map(function ($t1) use ($a) {
        $b = $t1->_1;
        $c = $t1->_2;
        return $b;
    });
});