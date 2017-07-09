--DESCRIPTION--

Test simplest one expression

--GIVEN--

for {
    $a <- Some(42)
} yield $a;

--EXPECT--

Some(42)->map(function ($a) {
    return $a;
});