--DESCRIPTION--

Test iteration

--GIVEN--

for ($a <- Some(1)) { echo $a; }

--EXPECT--

Some(1)->withEach(function ($a) {
    echo $a;
});