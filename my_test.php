<?php

$s = fopen(__DIR__ . "/font.font", "w");
// header without character data
fwrite($s, "\x01\x00\x00\x00\x20\x00\x00\x00\x08\x00\x00\x00\x08\x00\x00\x00");
fclose($s);
$font = imageloadfont(__DIR__ . "/font.font");
$im = imagecreate(10, 10);
imagechar($im, $font, 0, 0, " ", imagecolorallocate($im, 255, 255, 255));
