package com.example.car;

import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.springframework.boot.test.context.SpringBootTest;

import static org.mockito.Mockito.when;
import static org.springframework.test.util.AssertionErrors.assertEquals;

@SpringBootTest
public class SpringCarTest {
    @Mock
    DieselEngine engine;

    @Mock
    Suspension suspension;

    @InjectMocks
    Car car;

    @Test
    public void driveReturnsTrueWhenEngineAndSuspensionAreWorking() {

        when(suspension.work()).thenReturn(1);
        when(engine.work()).thenReturn(1);

        boolean isWorking = car.drive();
        assertEquals("Car is not working", true, isWorking);
    }

    @Test
    public void driveReturnsFalseWhenEngineAndSuspensionAreNotWorking() {
        Car car = new Car(engine, suspension);

        when(engine.work()).thenReturn(0);

        boolean isWorking = car.drive();
        assertEquals("Car is working", false, isWorking);
    }
}