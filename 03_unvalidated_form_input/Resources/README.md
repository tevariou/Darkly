# Unvalidated form input

## Vulnerability
* Go to `survey` category
* Inspect one of the form and add another optional value like this
```
<form action="#" method="post">
    <input type="hidden" name="sujet" value="3">
    <select name="valeur" onchange="javascript:this.form.submit();">
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
        <option value="4">4</option>
        <option value="5">5</option>
        <option value="6">6</option>
        <option value="7">7</option>
        <option value="8">8</option>
        <option value="9">9</option>
        <option value="10">10</option> 
        <option value="11">11</option> // added option
    </select>
</form>
```
* Select the previously inserted value in the form in order to get the flag

## Attack
An attacker can bypass client side validation and send out of scope inputs to
 the server

## Fix
Server side strict validation is primordial. Never trust the client.

## Reference
https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html
