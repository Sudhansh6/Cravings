const validate = () =>
{
    alert('validating');
    const form = document.getElementById('form');
    const message = document.getElementById('message');
    const regex = new RegExp(/\W/g);
    const regex2 = new RegExp(/0|1|2|3|4|5|6|7|8|9}/g);
    if (form.street.value.length>50)
    {
        message.innerHTML = '<h3>Enter an address with less than 50 characters</h3>';
    }
    else if (regex.test(form.street.value))
    {
        message.innerHTML = '<h3>Address should not contain any character other than alphabets and numbers</h3>';
    }
    else if (regex2.test(form.pin.value) || form.pin.value.length!=6)
    {
        message.innerHTML = '<h3>Enter a valid pin</h3>';
    }
    else if (regex2.test(form.pin.value) || form.pin.value.length!=10)
    {
        message.innerHTML = '<h3>Enter a valid phone number</h3>';
    }
    return false;
}