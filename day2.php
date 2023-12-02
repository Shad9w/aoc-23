<?php

$games = fopen("input.txt", "r") or die("Unable to open file!");
$games = fread($games,filesize("input.txt"));

$parsed_games = [];

$max = ["r" => 12, "g" => 13, "b" => 14];

$total = 0;
$total_power = 0;

foreach(explode(PHP_EOL, $games) as $game)
{
    if(!$game)
        break;

    $game_data = (explode(" ", $game));
    $game_idx = $game_data[1];
    $parsed_game = [];

    $parsed_game_data = ["b" => 0, "g" => 0, "r" => 0];

    foreach($game_data as $key => $data)
    {

        if($data[0] == "b" || $data[0] == "g" || $data[0] == "r")
        {
            $parsed_game_data[$data[0]] += $game_data[$key - 1];
        }

        if(preg_match('/;/', $data, $matches))
        {
            $parsed_game []= $parsed_game_data;
            $parsed_game_data = ["b" => 0, "g" => 0, "r" => 0];
        }
    }

    $parsed_game []= $parsed_game_data;

    $valid = true;

    foreach($parsed_game as $g)
    {
        if($g['b'] > $max['b'] || $g['r'] > $max['r'] || $g['g'] > $max['g'])
        {
            $valid = false;
        }
    }

    $max_cubes = ["r" => 0, "g" => 0, "b" => 0];

    foreach($parsed_game as $p)
    {
        foreach($p as $key => $val)
        {
            if($val > $max_cubes[$key])
            {
                $max_cubes[$key] = $val;
            }
        }
    }

    $power = $max_cubes["r"] * $max_cubes["g"] * $max_cubes["b"];
    $total_power += $power;
    
    if($valid)
    {
        $total += intval($game_idx);
    }
}

echo 'TOTAL:' .  $total . PHP_EOL;
echo 'TOTAL POWER:' .  $total_power;