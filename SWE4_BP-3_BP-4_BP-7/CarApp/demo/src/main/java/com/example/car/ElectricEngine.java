package com.example.car;

import org.springframework.stereotype.Component;

@Component("electricEngine")
public class ElectricEngine implements IEngine{
    public int work() {
        return 1;
    }
}
