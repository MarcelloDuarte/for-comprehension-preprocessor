--DESCRIPTION--

Test iteration

--GIVEN--

for ($a <- Some(1)) { echo $a; }

for ($a <- ImmList(1, 2, 3); $b <- ImmList($a); $c <- ImmList($b)) { echo $a + $b + $c; }

--EXPECT--

Some(1)->withEach(function($a) {
    echo $a;
});

ImmList(1, 2, 3)->withEach(function($a) {
    return ImmList($a)->withEach(function($b) {
        return ImmList($b)->withEach(function($c) {
            echo $a + $b + $c;
        });
    });
});