package com.example.car;


import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Component;

@Component
public class Car {

    IEngine engine;

    Suspension suspension;


   public Car(@Qualifier("dieselEngine") IEngine engine, Suspension suspension) {
        this.engine = engine;
        this.suspension = suspension;
    }

    public boolean drive() {
        if (engine.work() == 1 && suspension.work() == 1) {
            return true;
        }

        else {
            return false;
        }
    }
}
