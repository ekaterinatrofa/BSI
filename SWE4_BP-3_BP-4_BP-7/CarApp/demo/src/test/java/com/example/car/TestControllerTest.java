package com.example.car;

import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.Mockito;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
public class TestControllerTest {

    @Mock
    Car car;

    @InjectMocks
    TestController testController;

    @Test
    public void testCausesCarToDrive() {
        testController.test();

        Mockito.verify(car).drive();
    }
}
