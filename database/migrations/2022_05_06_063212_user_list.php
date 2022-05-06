<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up()
    {
        Schema::create('user_list', function (Blueprint $table) {
            $table->id();
            $table->integer('account_id')->unique();
            $table->text('number_phone');
        });
    }

    public function down()
    {
        Schema::dropIfExists('user_list');
    }
};
