<?php

namespace App\Http\Controllers;

use Laravel\Lumen\Routing\Controller as BaseController;
use Illuminate\Http\Request;

class MessageController extends BaseController
{
    public function postSendMessage(Request $request) {
        if ($request->input('account') !== null && $request->input('to') !== null && $request->input('message') !== null) {
            if (trim($request->input('account')) == '' || trim($request->input('to')) == '' || trim($request->input('message')) == '') {
                echo 'Запрос содержит пустые поля';
                return;
            }

            if (preg_match('/^\+?\d+$/', $request->input('to'))) {
                shell_exec('cd send-whatsapp && python whatbot.py ' . $request->input('to') . ' ' . $request->input('message'));

                echo 'account: ' . $request->input('account') 
                . PHP_EOL . 'to: ' . $request->input('to') 
                . PHP_EOL . 'message: ' . $request->input('message');
            }
            else
                echo '$request->input("to") is not int';
        }
        else
            echo 'Неверный формат запроса';
    }

    public function postMessageStatus(Request $request) {
        if ($request->input('status') !== null) {
            if (trim($request->input('status')) == '') {
                echo 'Запрос содержит пустые поля';
                return;
            }

            if (preg_match('/^\+?\d+$/', $request->input('status')))
                echo 'status: ' . $request->input('status');
            else
                echo '$request->input("status") is not int';
        }
        else
            echo 'Неверный формат запроса';
    }
}