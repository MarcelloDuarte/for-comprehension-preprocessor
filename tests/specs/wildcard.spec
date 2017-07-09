--DESCRIPTION--

Test wildcard

--GIVEN--

for {
    _ <- Some(42)
} yield ();

--EXPECT--

Some(42)->map(function ($_) {
    return Unit();
});