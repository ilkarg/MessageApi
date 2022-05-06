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
                if (strtolower($request->input('account')) == 'whatsapp')
                    shell_exec('cd public/send-whatsapp && python whatbot.py ' . $request->input('to') . ' ' . $request->input('message'));
                else if (strtolower($request->input('account')) == 'telegram')
                    shell_exec('cd public/send-telegram && python send_message.py ' . $request->input('to') . ' ' . $request->input('message'));
                else if (strtolower($request->input('account')) == 'vk' || strtolower($request->input('account')) == 'вк'
                || strtolower($request->input('account')) == 'vkontakte' || strtolower($request->input('account')) == 'вконтакте')
                    echo 'Отправляем во вконтакте';
                else 
                    echo 'Неверный тип account';
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