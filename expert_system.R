cat("============================================\n")
cat("Welcome to the Laptop Troubleshooting Assistant!\n")
cat("============================================\n\n")

cat("Please describe your issue or choose from examples below:\n")
cat("------------------------------------------------------------\n")
cat(" • battery not charging\n")
cat(" • laptop is slow\n")
cat(" • laptop overheating\n")
cat(" • wifi not working\n")
cat(" • screen not displaying\n")
cat("------------------------------------------------------------\n\n")

issue <- tolower(readline(prompt = "Enter issue: "))

if (grepl("battery", issue) && grepl("not charging", issue)) {
  advice <- "Check your power adapter or battery connection."
} else if (grepl("slow", issue)) {
  advice <- "Try closing unused programs or upgrading your RAM."
} else if (grepl("overheat", issue)) {
  advice <- "Clean your laptop’s fan and ensure proper ventilation."
} else if (grepl("wifi", issue)) {
  advice <- "Restart your router or update your Wi-Fi drivers."
} else if (grepl("screen", issue)) {
  advice <- "Check the display cable or connect to an external monitor to test."
} else {
  advice <- "Issue not recognized. Please contact technical support."
}


cat("\n============================================\n")
cat("Advice:", advice, "\n")
cat("============================================\n")
