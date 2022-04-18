<?php

/** @var \Laravel\Lumen\Routing\Router $router */

$router->get('/', function () use ($router) {
    return $router->app->version();
});


$router->post('/send_message', 'MessageController@postSendMessage');
$router->post('/status_message', 'MessageController@postMessageStatus');