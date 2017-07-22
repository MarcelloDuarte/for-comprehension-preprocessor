--DESCRIPTION--

Test simplest one expression

--GIVEN--

for {
    $a <- for {
        $b <- Some(42)
    } yield $b
} yield $a;

--EXPECT--

Some(42)->map(function ($b) {
    return $b;
})->map(function ($a) {
    return $a;
});