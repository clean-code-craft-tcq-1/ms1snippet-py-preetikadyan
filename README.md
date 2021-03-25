# Charge Validation Tool

This is a tool to validate charging parameters.

Given a set of values, it checks if they have 'sudden jumps'.
Such jumps indicate a failed / noisy sensor.

## Tasks

1. The 'No Duplications' check is failing. Resolve the duplication.
1. Give a good name to the function `_give_me_a_good_name`.
It is a boolean function, used in `if` statements.
Ensure that the `if` statement reads like a sentence after you rename the function.
1. The `values` parameter, given to the `validate...` function can be `None`.
Currently, the code does not handle that.
Ensure the code ignores a call with `None` and add a test for that.

**Solution**

1. Duplication was existing in the initial code because same line of code were being used for validating the readings for different battery parameters.
   So to remove the duplication I have used a single method called **validate_reading(values, last_but_one_value,limit)** which carry out the same functionality as the initial code by   taking different 'limit' values for different parameters(e.g.: for SOC it takes limit = 0.05, for CURRENT it takes limit = 0.1)

2. I have renamed the method _give_me_a_good_name to **'if_given_parameter_produces_noise()'.**

3. In order to check if the value parameter is None i have created a method '**if_length_is_not_none_then_validate_reading()**' which means that the values will be validated only when the length is not none. If the length is none then a message will be displayed on the console stating for which parameter the 'value' is None.
