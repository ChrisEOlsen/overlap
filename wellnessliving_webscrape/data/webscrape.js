let resultArr = []

function findFirstAncestorWithTag(element, tagName) {
    // Convert the tag name to uppercase to ensure case-insensitive matching
    tagName = tagName.toUpperCase();
    
    // Traverse upwards in the DOM tree
    while (element) {
        // Check if the current element's tag name matches the specified tag name
        if (element.tagName === tagName) {
            return element;
        }
        // Move to the parent element
        element = element.parentElement;
    }
    
    // Return null if no matching ancestor is found
    return null;
}
// Used for identifying the day of week by extracting the id of the closest parent element with the td tag
const daysArray = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

document.body.querySelectorAll(".js-schedule-list-minute-row").forEach(block => {
  const blockWithTypeAndTime = block.querySelector(".rs-schedule-list-sortable-block")
  const blockWithStaffAndUser = block.querySelectorAll(".css-schedule-list-block-info")
  if (blockWithStaffAndUser) {
    blockWithStaffAndUser.forEach(subBlock => {
      if (blockWithTypeAndTime) {
        const type = blockWithTypeAndTime.querySelector("a").textContent
        const time = blockWithTypeAndTime.querySelector("a").nextElementSibling.textContent

        const staffSpans = subBlock.firstChild.querySelectorAll("span")
        let staff = []
        staffSpans.forEach(span => staff.push(span.textContent))
        const attendanceNumberOrClient = subBlock.firstChild.nextElementSibling.querySelector("b").textContent
       
        const elementWithDayName = findFirstAncestorWithTag(block, 'td')
        const dayOfWeek = daysArray[parseInt(elementWithDayName.id.slice(-1)) - 1]

        const dataObj = {
          type: type,
          time: time,
          day: dayOfWeek,
          staff: staff,
          attendance: attendanceNumberOrClient,
        }

        resultArr.push(dataObj)
      }
    })
  }
})


console.log(resultArr)
