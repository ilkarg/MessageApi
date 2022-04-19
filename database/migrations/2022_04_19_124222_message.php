<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up()
    {
        Schema::create('message', function (Blueprint $table) {
            $table->id();
            $table->unsignedBigInteger('account_id');
            $table->foreign('account_id')->references('id')->on('account');
            $table->text('message');
            $table->integer('status');
            $table->unsignedBigInteger('method');
            $table->foreign('method')->references('messenger_id')->on('messenger_settings');
        });
    }

    public function down()
    {
        Schema::dropIfExists('message');
    }
};
