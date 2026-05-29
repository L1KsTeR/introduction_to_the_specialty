document.getElementById("splitForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const resultDiv = document.getElementById("result");
    const errorDiv = document.getElementById("error");
    resultDiv.classList.add("hidden");
    errorDiv.classList.add("hidden");

    const payload = {
        bill: parseFloat(document.getElementById("bill").value),
        tip_percent: parseFloat(document.getElementById("tip").value),
        people: parseInt(document.getElementById("people").value),
    };

    try {
        const res = await fetch("/api/calculate", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload),
        });

        const data = await res.json();

        if (!res.ok) {
            let msg = data.error || "Ошибка запроса";
            if (Array.isArray(msg)) msg = msg.join(". ");
            throw new Error(msg);
        }

        resultDiv.innerHTML = `
            <p>Чаевые: ${data.tip_amount} ₽</p>
            <p>Итого к оплате: ${data.total} ₽</p>
            <p><strong>Каждому: ${data.per_person} ₽</strong></p>
        `;
        resultDiv.classList.remove("hidden");
    } catch (err) {
        errorDiv.textContent = err.message || "Не удалось связаться с сервером";
        errorDiv.classList.remove("hidden");
    }
});
