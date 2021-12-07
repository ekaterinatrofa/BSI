## The task is to demonstrate the possibility of implementation on the selected code SWE4 BP-3, BP-4, BP-7.

### SWE.4.BP3: Perform static verification of software units.

Verify software units for correctness using the defined criteria for verification. Record the results of the static verification.

_Static verification may include static analysis, code reviews, checks against coding standards and guidelines, and other techniques._

---

### SWE.4.BP4: Test software units.

Test software units using the unit test specification according to the software unit verification strategy. Record the test results and logs.

---

### SWE.4.BP7: Summarize and communicate results.

Summarize the unit test results and static verification results and communicate them to all affected parties. 

_Providing all necessary information from the test case execution in a summary enables other parties to judge the consequences._

---

###### Selected repository:

[https://github.com/ekaterinatrofa/Notepad](https://github.com/ekaterinatrofa/carApp)

The selected tool for static code analysis is ***SonarLint*** 

```
SonarLint is a Free and Open Source IDE extension that identifies and helps you fix quality and security issues as you code.

It will help you in following ways:
- Identify the new bugs and the quality issues in Java, typescript and javascript code. 
  So, it’s like a good self-review of code changes.
- Code improvements and suggestions while writing code rather than running sonarQube afterwards.
- We can also run it for every class where we make any change.
- It can teach you what’s wrong with the code, show you best practices, and give you examples of fixes.
```

###### References: 

- [https://www.sonarlint.org/](https://www.sonarlint.org/)
- [https://medium.com/@tarunchhabra/using-sonarlint-with-sonarqube-in-intellij-ide-5128111d1b8d](https://medium.com/@tarunchhabra/using-sonarlint-with-sonarqube-in-intellij-ide-5128111d1b8d)



###### SonarLint reports

![](https://github.com/ekaterinatrofa/BSI/blob/master/SWE4_BP-3_BP-4_BP-7/CarApp/Report_1.JPG)

![](https://github.com/ekaterinatrofa/BSI/blob/master/SWE4_BP-3_BP-4_BP-7/CarApp/Report_2.JPG)


***JaCoCo*** was selected as a test coverage tool 

```
JaCoCo is used to keep track of unit test coverage in the codebase. 
Simply put, the tool calculates the coverage using a number of strategies e.g.: lines, class, methods, etc.
JaCoCo is bundled by default with the latest IntelliJ IDEA distribution, so there's no requirement to install the plugin separately.

When executing unit tests, we can select what coverage runner we need to use. 
We can run the test cases either at the project level or at the class level.

``` 
###### References: 

- [https://www.baeldung.com/java-static-analysis-tools](https://www.baeldung.com/java-static-analysis-tools)

###### Test coverage report

![](https://github.com/ekaterinatrofa/BSI/blob/master/SWE4_BP-3_BP-4_BP-7/CarApp/Report_coverage.JPG)

We built our test class and attached the Mockito extension to it: 
```@ExtendWith(MockitoExtension.class) ```

```java
@ExtendWith(MockitoExtension.class)
public class CarTest {
    //....
}
```

The most widely used annotation in Mockito is ```@Mock```.
We can use ```@Mock``` to create and inject mocked instances without having to call Mockito.mock manually.

```java
@Mock
DieselEngine engine;

@Mock
Suspension suspension;
```
In order for the tests to be recognized as such, we'll add the ```@Test annotation```.
We specify what to return when a method is called with ```when-thenReturn```.
The ```assertEquals()``` method compares two objects for equality.

```java
  @Test
    public void driveReturnsTrueWhenEngineAndSuspensionAreWorking() {
        Car car = new Car(engine, suspension);

        when(suspension.work()).thenReturn(1);
        when(engine.work()).thenReturn(1);

        boolean isWorking = car.drive();
        assertEquals("Car is not working", true, isWorking);
    }

```

Author:

_Kateryna Trofymenko_