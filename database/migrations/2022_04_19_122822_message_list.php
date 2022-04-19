<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up()
    {
        Schema::create('message_list', function (Blueprint $table) {
            $table->id();
            $table->text('message');
        });

        DB::table('message_list')->insert(['message' => 'Привет']);
        DB::table('message_list')->insert(['message' => 'Пока']);
        DB::table('message_list')->insert(['message' => 'Как дела?']);
    }

    public function down() 
    {
        Schema::dropIfExists('message_list');
    }
};
