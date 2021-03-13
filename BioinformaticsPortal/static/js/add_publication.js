function updateTypeName(select){
    let text = ['Journal Name', 'Conference Name']
    $('label[for="id_typeName"]').html(text[select.selectedIndex])
}