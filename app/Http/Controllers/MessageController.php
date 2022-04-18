<?php

namespace App\Http\Controllers;

use Laravel\Lumen\Routing\Controller as BaseController;
use Illuminate\Http\Request;

class MessageController extends BaseController
{
    public function postSendMessage(Request $request) {
        if ($request->input('account') !== null && $request->input('to') !== null && $request->input('message') !== null) {
            if (trim($request->input('account')) == '' || trim($request->input('to')) == '' || trim($request->input('message')) == '')
                echo 'Запрос содержит пустые поля';
            else
                echo 'account: ' . $request->input('account') 
                . PHP_EOL . 'to: ' . $request->input('to') 
                . PHP_EOL . 'message: ' . $request->input('message');
        }
        else
            echo 'Неверный формат запроса';
    }

    public function postMessageStatus(Request $request) {
        if ($request->input('status') !== null) {
            if (trim($request->input('status')) == '')
                echo 'Запрос содержит пустые поля';
            else
                echo 'status: ' . $request->input('status');
        }
        else
            echo 'Неверный формат запроса';
    }
}