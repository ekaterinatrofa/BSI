package com.example.car;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;

@RestController
public class MyController {
 ArrayList<String> carList = new ArrayList<>();

    @GetMapping("/cars")
    public List<String> getCar() {
        return carList;
    }

    @PostMapping("/cars/{carName}")
    public String addCar(@PathVariable String carName) {
        carList.add(carName);

        return carName;
    }
}
