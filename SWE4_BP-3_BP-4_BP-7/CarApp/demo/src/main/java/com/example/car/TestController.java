package com.example.car;

import org.springframework.beans.factory.annotation.Autowired;

public class TestController {

    @Autowired
    Car car;

    public void test() {
        car.drive();
    }
}
