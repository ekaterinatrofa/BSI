package com.example.car;

import org.springframework.stereotype.Component;

@Component("dieselEngine")
public class DieselEngine implements IEngine{
    public int work() {
        return 1;
    }
}
