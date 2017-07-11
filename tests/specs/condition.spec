--DESCRIPTION--

Test comprehension with condition

--GIVEN--

for ($a <- ImmList(1, 2, 3)) yield $a;

for ($a <- ImmList(1, 2, 3) if ($a % 2 == 0) ) yield $a;

for {
    $a <- ImmList(1, 2, 3) if ($a % 2 == 0)
} yield $a;

--EXPECT--

ImmList(1, 2, 3)->map(function ($a) {
    return $a;
});

ImmList(1, 2, 3)->filter(function ($a) {
    return $a % 2 == 0;
});

ImmList(1, 2, 3)->filter(function ($a) {
    return $a % 2 == 0;
});