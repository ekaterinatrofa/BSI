package com.example.car;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import static org.mockito.Mockito.when;
import static org.springframework.test.util.AssertionErrors.assertEquals;

@ExtendWith(MockitoExtension.class)
public class CarTest {
    @Mock
    DieselEngine engine;

    @Mock
    Suspension suspension;

    @Test
    public void driveReturnsTrueWhenEngineAndSuspensionAreWorking() {
        Car car = new Car(engine, suspension);

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