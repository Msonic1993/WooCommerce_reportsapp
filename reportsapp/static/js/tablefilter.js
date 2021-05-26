function filterTable() {

  var input, filter, filter1, table, tr, td, td0, i, txtValue;
  input = document.getElementById("inputSearch");
  filter = input.value.toUpperCase();
  filter1 = input.value.toUpperCase("Total:");
  table = document.getElementById("topproduct");
  tr = table.getElementsByTagName("tr");
  tfoot = table.getElementsByTagName("tfoot");


  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[1];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1)  {
        tr[i].style.display = "";

      } else {
        tr[i].style.display = "none";
      }
    }
  }


}