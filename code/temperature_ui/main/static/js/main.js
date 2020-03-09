$('#city_id').change(function() {
    $('#area_select').find('option').remove()
    $('#apartment_select').find('option').remove()
    $('#house_select').find('option').remove()
    window.city_id = $('#city_id').val()
    let xhr = new XMLHttpRequest(),
        url = 'http://127.0.0.1:8000/get_areas_list?city_id=' + window.city_id
    xhr.onreadystatechange = function() {
        if (xhr.readyState == XMLHttpRequest.DONE) {
            response = JSON.parse(xhr.responseText)
            areas_count = response.areas_count
            $('#area_select').append($("<option></option>").text('Не выбрано'));
            for (i = 1; i <= areas_count; i++){
                $('#area_select').append($("<option></option>").attr("value", i).text(i));
            }
        }
    }
    xhr.open('GET', url, true);
    xhr.send();


})

$('#area_select').change(function() {
    $('#apartment_select').find('option').remove()
    $('#house_select').find('option').remove()
    window.area_id = $('#area_select').val()
    let xhr = new XMLHttpRequest(),
        url = `http://127.0.0.1:8000/get_houses_list?city_id=${window.city_id}&area_id=${window.area_id}`

    xhr.onreadystatechange = function() {
        if (xhr.readyState == XMLHttpRequest.DONE) {
            response = JSON.parse(xhr.responseText)
            $('#house_select').append($("<option></option>").text('Не выбрано'));
            response.forEach((house, i) => {

                $('#house_select').append($("<option></option>").attr("value", house.house_id).text(house.house_id));
            });

        }
    }
    xhr.open('GET', url, true);
    xhr.send();

})
$('#house_select').change(function() {
    $('#apartment_select').find('option').remove()
    window.house_id = $('#house_select').val()
    let xhr = new XMLHttpRequest(),
        url = `http://127.0.0.1:8000/get_apartment_list?city_id=${window.city_id}&area_id=${window.area_id}&house_id=${window.house_id}`

    xhr.onreadystatechange = function() {
        if (xhr.readyState == XMLHttpRequest.DONE) {
            response = JSON.parse(xhr.responseText)
            window.apartment_count = response
            $('#apartment_select').append($("<option></option>").text('Не выбрано'));

            for (i = 1; i <= apartment_count; i++){
                $('#apartment_select').append($("<option></option>").attr("value", i).text(i));
            }

        }
    }
    xhr.open('GET', url, true);
    xhr.send();

})
