function animateCounter(elementId, target, duration, suffix = "") {
    const counterElement = document.getElementById(elementId);
    let current = 0;

    const interval = setInterval(() => {
        counterElement.textContent = current;
        current++;

        if (current > target) {
            clearInterval(interval);
            counterElement.textContent = target + suffix;
        }
    }, duration / (target + 1));
}

animateCounter("firstcounter", 100, 1550, " + finished projects");
animateCounter("secondcounter", 5, 1550, " + years we work");
animateCounter("thirdcounter", 100, 1550, " +");