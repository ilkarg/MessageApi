<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up()
    {
        Schema::create('messenger_settings', function (Blueprint $table) {
            $table->id('messenger_id');
            $table->unsignedBigInteger('account_id');
            $table->foreign('account_id')->references('id')->on('account');
            $table->json('settings');
        });
    }

    public function down()
    {
        Schema::dropIfExists('messenger_settings');
    }
};
