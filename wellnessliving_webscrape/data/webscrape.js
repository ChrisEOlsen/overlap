let resultArr = []
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

        const dataObj = {
          type: type,
          time: time,
          staff: staff,
          attendance: attendanceNumberOrClient,
        }

        resultArr.push(dataObj)
      }
    })
  }
})

