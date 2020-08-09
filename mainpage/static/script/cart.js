const add = (e) => {
    const item = e.getAttribute('data-item');
    const request = new XMLHttpRequest();
    request.open('POST', '/');
    alert('Sent request')
    request.onload = () => {
        alert('Item succesfully added to cart.')
    }
    const data = new FormData();
    data.append('id', item);
    request.send(data);
}