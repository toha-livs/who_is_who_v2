$(function() {
    console.log($('#resultts').text())
    if ($('#resultts').text() == '5') {
        $('#win').attr('src', 'https://i.gifer.com/y3.gif')
    }
    else if ($('#resultts').text() == '4') {
        $('#win').attr('src', 'https://i.gifer.com/4FB4.gif')
    }
    else if ($('#resultts').text() == '3') {
        $('#win').attr('src', 'https://i.gifer.com/JQd.gif')
    }
     else if ($('#resultts').text() == '2') {
        $('#win').attr('src', 'https://i.gifer.com/7VE.gif')
    }
    else if ($('#resultts').text() == '1') {
        $('#win').attr('src', 'https://i.gifer.com/WG8S.gif')
    }})