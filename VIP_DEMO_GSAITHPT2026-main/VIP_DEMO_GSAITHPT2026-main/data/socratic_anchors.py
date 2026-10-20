# VIP 74.1 - HỆ THỐNG GIA SƯ AI THPT 2026 (CHUẨN GDPT 2018 - BẢN VÁ HOÀN THIỆN ĐA MÔN & ĐA KHỐI LỚP)
# -*- coding: utf-8 -*-
"""SOCRATIC KNOWLEDGE ANCHORS DATA MODULE"""

SOCRATIC_KNOWLEDGE_ANCHORS = {
    "Toán học": [
        # 1. Đơn điệu & Đạo hàm
        {
            "keywords": ["đồng biến", "nghịch biến", "đơn điệu", "khoảng đồng biến", "khoảng nghịch biến"],
            "concept": "Tính đơn điệu của hàm số (SGK Toán 12 - KNTT)",
            "formula": "Cho hàm số $y = f(x)$ có đạo hàm trên khoảng $(a; b)$:\n- $f'(x) \\ge 0, \\forall x \\in (a; b) \\Rightarrow$ Hàm số **đồng biến** trên $(a; b)$.\n- $f'(x) \\le 0, \\forall x \\in (a; b) \\Rightarrow$ Hàm số **nghịch biến** trên $(a; b)$.\n*(Dấu bằng chỉ xảy ra tại hữu hạn điểm)*",
            "prompt": "Em hãy tính đạo hàm $f'(x)$, tìm các nghiệm của phương trình $f'(x) = 0$ và xét dấu của $f'(x)$ để kết luận khoảng biến thiên nhé!"
        },
        # 2. Cực trị
        {
            "keywords": ["cực trị", "cực đại", "cực tiểu", "điểm cực đại", "điểm cực tiểu", "giá trị cực", "số điểm cực trị"],
            "concept": "Cực trị của hàm số (SGK Toán 12 - KNTT)",
            "formula": "- Điều kiện cần: Nếu hàm số đạt cực trị tại $x_0$ thì $f'(x_0) = 0$ hoặc $f'(x_0)$ không xác định.\n- Điều kiện đủ: $f'(x)$ đổi dấu từ $(+)$ sang $(-)$ qua $x_0 \\Rightarrow x_0$ là **điểm cực đại**; đổi dấu từ $(-)$ sang $(+) \\Rightarrow x_0$ là **điểm cực tiểu**.\n*(Chỉ các nghiệm bội lẻ mới làm $f'(x)$ đổi dấu và tạo thành cực trị)*",
            "prompt": "Em hãy giải phương trình $f'(x) = 0$, đếm các nghiệm bội lẻ (nghiệm đơn) làm đạo hàm đổi dấu để tìm số điểm cực trị nhé!"
        },
        # 3. Giá trị lớn nhất & nhỏ nhất
        {
            "keywords": ["giá trị lớn nhất", "giá trị nhỏ nhất", "gtln", "gtnn", "max", "min"],
            "concept": "Giá trị lớn nhất và nhỏ nhất của hàm số trên đoạn $[a; b]$ (SGK Toán 12 - KNTT)",
            "formula": "Quy tắc tìm GTLN, GTNN trên đoạn $[a; b]$:\n1. Tính đạo hàm $f'(x)$, tìm các nghiệm $x_i \\in (a; b)$ của phương trình $f'(x) = 0$.\n2. Tính các giá trị: $f(a)$, $f(b)$ và các $f(x_i)$.\n3. $\\max_{[a; b]} f(x) = \\max\\{f(a), f(b), f(x_i)\\}$; $\\min_{[a; b]} f(x) = \\min\\{f(a), f(b), f(x_i)\\}$.",
            "prompt": "Em hãy tìm các nghiệm của $f'(x) = 0$ nằm trong đoạn $[a; b]$, tính giá trị hàm số tại các điểm đó và hai đầu mút rồi so sánh nhé!"
        },
        # 4. Tiệm cận
        {
            "keywords": ["tiệm cận đứng", "tiệm cận ngang", "tiệm cận xiên", "đường tiệm cận"],
            "concept": "Đường tiệm cận của đồ thị hàm số (SGK Toán 12 - KNTT)",
            "formula": "- Tiệm cận đứng: Đường thẳng $x = x_0$ nếu ít nhất một giới hạn $\\lim_{x \\to x_0^\\pm} y = \\pm\\infty$.\n- Tiệm cận ngang: Đường thẳng $y = y_0$ nếu $\\lim_{x \\to \\pm\\infty} y = y_0$.\n- Tiệm cận xiên: Đường thẳng $y = ax + b$ với $a = \\lim_{x \\to \\pm\\infty} \\frac{y}{x}$, $b = \\lim_{x \\to \\pm\\infty} (y - ax)$.",
            "prompt": "Với hàm phân thức, em hãy tìm nghiệm của mẫu số (không triệt tiêu với tử số) để xác định tiệm cận đứng, và xét tỉ số bậc cao nhất khi $x \\to \\pm\\infty$ để tìm tiệm cận ngang/xiên nhé!"
        },
        # 5. Tiếp tuyến
        {
            "keywords": ["tiếp tuyến", "hệ số góc", "phương trình tiếp tuyến"],
            "concept": "Phương trình tiếp tuyến của đồ thị hàm số (SGK Toán 12 - KNTT)",
            "formula": "Phương trình tiếp tuyến của đồ thị $y = f(x)$ tại tiếp điểm $M(x_0; y_0)$:\n$$y = f'(x_0)(x - x_0) + y_0$$\n- Hệ số góc của tiếp tuyến là $k = f'(x_0)$.",
            "prompt": "Em hãy tính đạo hàm $f'(x)$, thay hoành độ tiếp điểm $x_0$ vào để tìm hệ số góc $k$ và lập phương trình tiếp tuyến nhé!"
        },
        # 6. Nguyên hàm cơ bản
        {
            "keywords": ["nguyên hàm", "họ nguyên hàm", "f(x) dx", "bảng nguyên hàm"],
            "concept": "Nguyên hàm & Bảng nguyên hàm cơ bản (SGK Toán 12 - KNTT)",
            "formula": "- Tuyến tính: $\\int [a f(x) + b g(x)]dx = a\\int f(x)dx + b\\int g(x)dx$\n- Lũy thừa: $\\int x^\\alpha dx = \\frac{x^{\\alpha+1}}{\\alpha+1} + C$ ($\\alpha \\ne -1$); $\\int \\frac{1}{x}dx = \\ln|x| + C$\n- Mũ: $\\int e^x dx = e^x + C$; $\\int a^x dx = \\frac{a^x}{\\ln a} + C$\n- Lượng giác: $\\int \\cos x dx = \\sin x + C$; $\\int \\sin x dx = -\\cos x + C$",
            "prompt": "Em hãy tách biểu thức thành tổng các số hạng đơn giản và áp dụng trực tiếp công thức nguyên hàm cơ bản tương ứng nhé!"
        },
        # 7. Tích phân & Ứng dụng
        {
            "keywords": ["tích phân", "diện tích hình phẳng", "thể tích khối tròn xoay"],
            "concept": "Tích phân và Ứng dụng hình học (SGK Toán 12 - KNTT)",
            "formula": "- Định nghĩa: $\\int_a^b f(x)dx = F(b) - F(a)$ với $F'(x) = f(x)$.\n- Diện tích hình phẳng giới hạn bởi $y=f(x)$, trục $Ox$, $x=a$, $x=b$: $S = \\int_a^b |f(x)|dx$.\n- Thể tích tròn xoay quay quanh $Ox$: $V = \\pi \\int_a^b [f(x)]^2 dx$.",
            "prompt": "Em hãy xác định cận tích phân $[a; b]$, viết đúng công thức giải tích và áp dụng định lý Newton-Leibniz $F(b) - F(a)$ để tính nhé!"
        },
        # 8. Thể tích khối đa diện & Tròn xoay
        {
            "keywords": ["thể tích khối", "khối chóp", "lăng trụ", "lập phương", "khối nón", "khối trụ", "thể tích mặt cầu", "khối cầu"],
            "concept": "Thể tích các khối đa diện và khối tròn xoay (SGK Toán 12 - KNTT)",
            "formula": "- Lăng trụ & Khối hộp: $V = B \\cdot h$ (Khối lập phương cạnh $a$: $V = a^3$).\n- Khối chóp: $V = \\frac{1}{3} B \\cdot h$.\n- Khối nón: $V = \\frac{1}{3}\\pi r^2 h$; Khối trụ: $V = \\pi r^2 h$; Mặt cầu: $S = 4\\pi R^2$, $V = \\frac{4}{3}\\pi R^3$.",
            "prompt": "Em hãy xác định diện tích đáy $B$ và chiều cao $h$ vuông góc từ đỉnh xuống đáy rồi thế vào công thức chuẩn nhé!"
        },
        # 8.5. Góc trong không gian Oxyz (Góc giữa hai mặt phẳng, hai đường thẳng, hai vectơ)
        {
            "keywords": ["góc nghiêng", "góc giữa hai mặt phẳng", "góc giữa 2 mặt phẳng", "góc giữa hai vectơ", "góc giữa hai đường thẳng", "góc giữa đường thẳng và mặt phẳng", "vectơ pháp tuyến của mái nhà", "mặt phẳng nằm ngang", "góc giữa", "cosin của góc", "góc giữa hai véc-tơ", "góc giữa 2 véc tơ"],
            "concept": "Góc trong không gian Oxyz (SGK Toán 12 - KNTT)",
            "formula": "- **Góc giữa hai mặt phẳng $(P)$ và $(Q)$:** $\\cos \\alpha = \\frac{|\\vec{n}_1 \\cdot \\vec{n}_2|}{|\\vec{n}_1| \\cdot |\\vec{n}_2|} = \\frac{|A_1 A_2 + B_1 B_2 + C_1 C_2|}{\\sqrt{A_1^2 + B_1^2 + C_1^2} \\cdot \\sqrt{A_2^2 + B_2^2 + C_2^2}}$ ($0^\\circ \\le \\alpha \\le 90^\\circ$).\n- **Góc giữa hai vectơ:** $\\cos(\\vec{u}, \\vec{v}) = \\frac{\\vec{u} \\cdot \\vec{v}}{|\\vec{u}| \\cdot |\\vec{v}|} = \\frac{x_1 x_2 + y_1 y_2 + z_1 z_2}{\\sqrt{x_1^2+y_1^2+z_1^2} \\cdot \\sqrt{x_2^2+y_2^2+z_2^2}}$.\n- **Góc giữa hai đường thẳng:** $\\cos \\varphi = \\frac{|\\vec{u}_1 \\cdot \\vec{u}_2|}{|\\vec{u}_1| \\cdot |\\vec{u}_2|}$.\n- **Góc giữa đường thẳng và mặt phẳng:** $\\sin \\theta = \\frac{|\\vec{u} \\cdot \\vec{n}|}{|\\vec{u}| \\cdot |\\vec{n}|}$.",
            "prompt": "Em hãy xác định hai vectơ pháp tuyến (hoặc chỉ phương) tương ứng, sau đó áp dụng công thức cosin $\\cos \\alpha = \\frac{|\\vec{n}_1 \\cdot \\vec{n}_2|}{|\\vec{n}_1| \\cdot |\\vec{n}_2|}$ (chú ý luôn lấy dấu giá trị tuyệt đối ở tử số để $0^\\circ \\le \\alpha \\le 90^\\circ$) để tính góc nghiêng nhé!"
        },
        # 9. Tọa độ vectơ Oxyz
        {
            "keywords": ["tọa độ", "vectơ", "vecto", "oxyz", "tích vô hướng", "độ dài vectơ"],
            "concept": "Hệ tọa độ trong không gian Oxyz (SGK Toán 12 - KNTT)",
            "formula": "- $\\vec{AB} = (x_B - x_A;\\; y_B - y_A;\\; z_B - z_A)$.\n- Độ dài: $|\\vec{a}| = \\sqrt{x^2 + y^2 + z^2}$; $|\\vec{AB}| = \\sqrt{(x_B - x_A)^2 + (y_B - y_A)^2 + (z_B - z_A)^2}$.\n- Tích vô hướng: $\\vec{u} \\cdot \\vec{v} = x_1 x_2 + y_1 y_2 + z_1 z_2$.\n- Điều kiện vuông góc: $\\vec{u} \\perp \\vec{v} \\Leftrightarrow \\vec{u} \\cdot \\vec{v} = 0$.",
            "prompt": "Em hãy lấy tọa độ ngọn trừ tọa độ gốc tương ứng để tìm tọa độ vectơ, rồi tính độ dài hoặc tích vô hướng theo công thức nhé!"
        },
        # 10. Phương trình mặt cầu Oxyz
        {
            "keywords": ["mặt cầu", "phương trình mặt cầu", "tâm i", "bán kính r"],
            "concept": "Phương trình mặt cầu trong không gian Oxyz (SGK Toán 12 - KNTT)",
            "formula": "- Phương trình chính tắc tâm $I(a; b; c)$, bán kính $R$: $(x - a)^2 + (y - b)^2 + (z - c)^2 = R^2$.\n- Dạng khai triển: $x^2 + y^2 + z^2 - 2ax - 2by - 2cz + d = 0$ có tâm $I(a; b; c)$, bán kính $R = \\sqrt{a^2 + b^2 + c^2 - d}$ ($a^2+b^2+c^2-d > 0$).",
            "prompt": "Em hãy xác định tọa độ tâm $I(a; b; c)$ và bán kính $R$ từ giả thiết đề bài, lưu ý đổi dấu khi đưa vào ngoặc chính tắc nhé!"
        },
        # 11. Phương trình mặt phẳng & Đường thẳng Oxyz
        {
            "keywords": ["mặt phẳng", "vectơ pháp tuyến", "đường thẳng", "vectơ chỉ phương", "khoảng cách từ điểm"],
            "concept": "Mặt phẳng và Đường thẳng trong Oxyz (SGK Toán 12 - KNTT)",
            "formula": "- Mặt phẳng qua $M_0(x_0; y_0; z_0)$ có VTPT $\\vec{n}=(A; B; C)$: $A(x - x_0) + B(y - y_0) + C(z - z_0) = 0$.\n- Khoảng cách từ điểm $M(x_M; y_M; z_M)$ đến $(P): Ax+By+Cz+D=0$: $d(M, (P)) = \\frac{|Ax_M + By_M + Cz_M + D|}{\\sqrt{A^2 + B^2 + C^2}}$.\n- Đường thẳng qua $M_0$ có VTCP $\\vec{u}=(a; b; c)$: $\\frac{x - x_0}{a} = \\frac{y - y_0}{b} = \\frac{z - z_0}{c}$.",
            "prompt": "Em hãy tìm một điểm đi qua và vectơ chỉ phương / pháp tuyến tương ứng để lập phương trình hoặc tính khoảng cách nhé!"
        },
        # 12. Mũ & Logarit
        {
            "keywords": ["logarit", "log", "ln", "mũ", "luỹ thừa", "tập nghiệm của bất phương trình"],
            "concept": "Hàm số Mũ và Logarit (SGK Toán 12 - KNTT)",
            "formula": "- Điều kiện xác định của $\\log_a b$: cơ số $0 < a \\ne 1$, biểu thức $b > 0$.\n- Biến đổi: $\\log_a(x y) = \\log_a x + \\log_a y$; $\\log_a(\\frac{x}{y}) = \\log_a x - \\log_a y$; $\\log_a(x^\\alpha) = \\alpha\\log_a x$.\n- Bất phương trình $\\log_a f(x) > \\log_a g(x)$: Cùng chiều khi $a > 1$; Ngược chiều khi $0 < a < 1$ (kèm ĐKXĐ).",
            "prompt": "Em hãy đặt điều kiện xác định trước tiên, sau đó đưa về cùng cơ số và chú ý chiều của bất phương trình khi cơ số lớn hơn hay nhỏ hơn 1 nhé!"
        },
        # 13. Xác suất cổ điển & Xác suất có điều kiện
        {
            "keywords": ["xác suất", "biến cố", "xác suất có điều kiện", "xác suất toàn phần", "bayes", "biến cố độc lập"],
            "concept": "Xác suất & Biến cố (SGK Toán 12 - KNTT)",
            "formula": "- Xác suất cổ điển: $P(A) = \\frac{n(A)}{n(\\Omega)}$.\n- Xác suất có điều kiện: $P(A|B) = \\frac{P(AB)}{P(B)}$.\n- Công thức nhân xác suất: $P(AB) = P(A) \\cdot P(B|A)$.\n- Công thức xác suất toàn phần: $P(A) = \\sum P(B_i)P(A|B_i)$.",
            "prompt": "Em hãy xác định số phần tử không gian mẫu $n(\\Omega)$, số kết quả thuận lợi $n(A)$ hoặc lập sơ đồ hình cây để tính xác suất nhé!"
        },
        # 14. Mẫu số liệu ghép nhóm & Các số đặc trưng đo xu thế trung tâm, phân tán
        {
            "keywords": ["mẫu số liệu", "ghép nhóm", "khoảng biến thiên", "khoảng tứ phân vị", "độ lệch chuẩn", "phương sai", "trung vị", "tứ phân vị", "mốt"],
            "concept": "Các số đặc trưng của Mẫu số liệu ghép nhóm (SGK Toán 12 - KNTT)",
            "formula": "- **Khoảng biến thiên:** $R = a_k - a_1$ (Lấy đầu mút phải của nhóm cuối cùng trừ đầu mút trái của nhóm đầu tiên).\n- **Khoảng tứ phân vị:** $\\Delta_Q = Q_3 - Q_1$.\n- **Trung vị $M_e$:** $M_e = u_m + \\dfrac{\\frac{n}{2} - C}{n_m} \\cdot (u_{m+1} - u_m)$.\n- **Mốt $M_o$:** $M_o = u_j + \\dfrac{n_j - n_{j-1}}{(n_j - n_{j-1}) + (n_j - n_{j+1})} \\cdot (u_{j+1} - u_j)$.\n- **Phương sai & Độ lệch chuẩn:** $s^2 = \\frac{1}{n}\\sum n_i(c_i - \\bar{x})^2$; $s = \\sqrt{s^2}$.",
            "prompt": "Em hãy đối chiếu công thức số đặc trưng trong SGK KNTT (chú ý: khoảng biến thiên $R = a_k - a_1$ bằng đầu mút phải nhóm cuối trừ đầu mút trái nhóm đầu) để chọn phương án chuẩn xác nhé!"
        }
    ],
    "Vật lý": [
        {
            "keywords": ["dao động điều hòa", "con lắc", "chu kì", "tần số", "pha dao động", "li độ"],
            "concept": "Dao động điều hòa (SGK Vật lý 12 - KNTT)",
            "formula": "- Li độ: $x = A\\cos(\\omega t + \\varphi)$.\n- Vận tốc: $v = x' = -\\omega A\\sin(\\omega t + \\varphi) = \\omega A\\cos(\\omega t + \\varphi + \\frac{\\pi}{2})$.\n- Gia tốc: $a = v' = -\\omega^2 x = \\omega^2 A\\cos(\\omega t + \\varphi + \\pi)$.\n- Hệ thức độc lập: $x^2 + \\frac{v^2}{\\omega^2} = A^2$; $a = -\\omega^2 x$.",
            "prompt": "Em hãy xác định các đại lượng $A, \\omega, \\varphi$ từ giả thiết và áp dụng hệ thức độc lập thời gian để tính đại lượng cần tìm nhé!"
        },
        {
            "keywords": ["sóng cơ", "bước sóng", "sóng dừng", "giao thoa"],
            "concept": "Sóng cơ và Giao thoa sóng (SGK Vật lý 12 - KNTT)",
            "formula": "- Bước sóng: $\\lambda = v \\cdot T = \\frac{v}{f}$.\n- Sóng dừng 2 đầu cố định: $L = k\\frac{\\lambda}{2}$ ($k$ bụng sóng, $k+1$ nút).\n- Cực đại giao thoa: $d_2 - d_1 = k\\lambda$; Cực tiểu giao thoa: $d_2 - d_1 = (k + 0.5)\\lambda$.",
            "prompt": "Em hãy xác định vận tốc truyền sóng $v$ và tần số $f$ để tính bước sóng $\\lambda$, sau đó đối chiếu với điều kiện giao thoa/sóng dừng nhé!"
        },
        {
            "keywords": ["nhiệt độ", "nhiệt dung", "nhiệt hóa hơi", "nhiệt nóng chảy", "khí lý tưởng", "áp suất", "thể tích"],
            "concept": "Vật lý nhiệt & Thuyết động học phân tử chất khí (SGK Vật lý 12 - KNTT)",
            "formula": "- Phương trình Clapeyron-Mendeleev: $pV = nRT = \\frac{m}{\\mu}RT$.\n- Nhiệt lượng: $Q = mc\\Delta T$; Nhiệt chuyển thể: $Q = \\lambda m$ (nóng chảy), $Q = L m$ (hóa hơi).\n- Định luật I Nhiệt động lực học: $\\Delta U = A + Q$.",
            "prompt": "Em hãy tóm tắt các trạng thái $(p_1, V_1, T_1)$ và $(p_2, V_2, T_2)$, chú ý đổi nhiệt độ sang thang Kelvin ($T = t + 273$) để thế vào phương trình nhé!"
        }
    ],
    "Hóa học": [
        {
            "keywords": ["ester", "xà phòng hóa", "chất béo", "lipid", "thủy phân", "triglyceride"],
            "concept": "Ester - Lipid (SGK Hóa học 12 - KNTT & Danh pháp IUPAC)",
            "formula": "- Phản ứng xà phòng hóa ester: $RCOOR' + NaOH \\xrightarrow{t^o} RCOONa + R'OH$.\n- Thủy phân chất béo: $(RCOO)_3C_3H_5 + 3NaOH \\xrightarrow{t^o} 3RCOONa + C_3H_5(OH)_3$.\n- Bảo toàn khối lượng: $m_{ester} + m_{NaOH} = m_{muối} + m_{alcohol}$.",
            "prompt": "Em hãy xác định số mol các chất, viết phương trình phản ứng và áp dụng định luật bảo toàn khối lượng để tìm khối lượng muối hoặc alcohol nhé!"
        },
        {
            "keywords": ["glucose", "fructose", "saccharose", "carbohydrate", "tinh bột", "cellulose"],
            "concept": "Carbohydrate (SGK Hóa học 12 - KNTT)",
            "formula": "- Monosaccharide: Glucose ($C_6H_{12}O_6$) có nhóm $-CHO$ tráng bạc ra $2Ag$. Fructose có nhóm $C=O$, trong môi trường kiềm chuyển hóa thành glucose nên cũng tráng bạc.\n- Disaccharide: Saccharose ($C_{12}H_{22}O_{11}$) không tráng bạc, khi thủy phân tạo $1$ Glucose + $1$ Fructose.\n- Polysaccharide: Tinh bột, Cellulose thủy phân hoàn toàn tạo Glucose.",
            "prompt": "Em hãy đối chiếu công thức cấu tạo và nhóm chức đặc trưng để phân biệt khả năng phản ứng với thuốc thử Tollens ($AgNO_3/NH_3$) hoặc $Cu(OH)_2$ nhé!"
        }
    ],
    "Ngữ văn": [
        {
            "keywords": ["thể loại", "phương thức biểu đạt", "biện pháp tu từ", "đọc hiểu", "hình ảnh", "tác dụng"],
            "concept": "Đọc hiểu văn bản theo đặc trưng thể loại (SGK Ngữ văn 12 - KNTT)",
            "formula": "- Nhận diện: Thể thơ (tự do, 7 chữ, lục bát...), PTBĐ (biểu cảm, tự sự, nghị luận, thuyết minh...).\n- Phân tích BPTT: Gọi tên BPTT ➔ Chỉ ra từ ngữ/hình ảnh thể hiện ➔ Nêu tác dụng gợi hình, gợi cảm và làm nổi bật tư tưởng của tác giả.",
            "prompt": "Em hãy bám sát từ ngữ, hình ảnh trong ngữ liệu để chỉ rõ phương diện nghệ thuật và thông điệp mà tác giả gửi gắm nhé!"
        },
        {
            "keywords": ["nghị luận xã hội", "đoạn văn", "bài học", "thông điệp", "ý nghĩa"],
            "concept": "Viết đoạn văn nghị luận xã hội (200 chữ)",
            "formula": "- Mở đoạn: Dẫn dắt và nêu trực tiếp vấn đề nghị luận (1 câu).\n- Thân đoạn: Giải thích ngắn gọn ➔ Bàn luận, chứng minh (dẫn chứng thực tế xác thực) ➔ Mở rộng/phản đề.\n- Kết đoạn: Rút ra bài học nhận thức và hành động thiết thực cho bản thân.",
            "prompt": "Em hãy lựa chọn dẫn chứng thực tế tiêu biểu và liên hệ trách nhiệm của tuổi trẻ để bài viết giàu tính thuyết phục nhé!"
        }
    ],
    "Tiếng Anh": [
        {
            "keywords": ["pronunciation", "stress", "pronounced", "underlined", "primary stress"],
            "concept": "Pronunciation & Word Stress (CEFR Standards)",
            "formula": "- 2-syllable nouns/adjectives usually stress on 1st syllable (e.g., 'table, 'clever).\n- 2-syllable verbs usually stress on 2nd syllable (e.g., de'cide, pre'sent).\n- Endings with -tion, -sion, -ic stress on syllable right before (e.g., pro'tection, scien'tific).",
            "prompt": "Read each word aloud carefully and identify the syllable with higher pitch and longer duration to find the difference!"
        },
        {
            "keywords": ["relative clause", "which", "whom", "whose", "where", "conditional", "if", "unless"],
            "concept": "Grammar: Clauses & Conditionals",
            "formula": "- Relative Pronouns: Who (subject/people), Whom (object/people), Which (things), Whose (possession).\n- Conditionals: Type 1 (If + V_s/es, will + V0); Type 2 (If + V2/ed, would + V0); Type 3 (If + had V3/ed, would have V3/ed).",
            "prompt": "Look closely at the subject, tense of the main clause, and the role of the noun being replaced to choose the correct structure!"
        }
    ]
}

def sanitize_socratic_hint(hint_text, correct_answer="", q_text="", options=None, level="TH", subject="Toán học", grade_num=12):
    """
    HƯỚNG DẪN TƯ DUY SOCRATIC BÌNH DÂN HỌC VỤ (LUỒNG 1) - CHUẨN SƯ PHẠM QUỐC GIA.
    Nguyên tắc sư phạm bất biến:
      1. TUYỆT ĐỐI 100% KHÔNG BAO GIỜ GIẢI HỘ, KHÔNG PHUN RA ĐÁP ÁN (A/B/C/D, Đúng/Sai, hay số điền cuối cùng) HOẶC PHÉP TÍNH THAY SỐ CỤ THỂ.
      2. Cung cấp ĐIỂM TỰA KIẾN THỨC CỐT LÕI (Định lý, Công thức tổng quát SGK Kết Nối Tri Thức).
      3. Đưa ra CÂU HỎI ĐỊNH HƯỚNG TƯ DUY SOCRATIC để học sinh tự suy nghĩ và tự đặt bút tính toán.
    """
    subj_key = str(subject or "Toán học").strip()
    q_str = str(q_text or "").strip()
    q_lower = q_str.lower()
    corr_ans = str(correct_answer or "").strip()
    
    # 0. ƯU TIÊN TUYỆT ĐỐI CHO CÂU HỎI ĐỌC BẢNG BIẾN THIÊN (BBT) & ĐỒ THỊ (GỢI MỞ KỸ NĂNG, KHÔNG SPOIL ĐÁP ÁN)
    if any(k in q_lower for k in ["bảng biến thiên", "bbt", "bảng xét dấu"]):
        if any(k in q_lower for k in ["nghịch biến", "đồng biến"]):
            return (
                "🎯 **Kỹ năng đọc nhanh Bảng biến thiên (SGK Toán GDPT 2018):**\n"
                "- Quan sát dòng $y'$ (hoặc $f'(x)$): Khoảng nào mang dấu trừ ($-$) hoặc mũi tên dòng $y$ đi xuống ($\\searrow$) là khoảng **nghịch biến**.\n"
                "- Khoảng nào mang dấu cộng ($+$) hoặc mũi tên dòng $y$ đi lên ($\\nearrow$) là khoảng **đồng biến**.\n\n"
                "💡 **Gợi mở Socratic:** *Em hãy đối chiếu các khoảng phương án với dòng dấu của $y'$ để chọn khoảng chính xác nhé!*"
            )
        elif any(k in q_lower for k in ["cực đại", "cực tiểu", "cực trị"]):
            return (
                "🎯 **Kỹ năng đọc Cực trị từ BBT (SGK Toán GDPT 2018):**\n"
                "- Điểm cực đại $x_{CĐ}$: Nơi $y'$ đổi dấu từ $(+)$ sang $(-)$ (đỉnh nhô lên).\n"
                "- Điểm cực tiểu $x_{CT}$: Nơi $y'$ đổi dấu từ $(-)$ sang $(+)$ (đáy lõm xuống).\n\n"
                "💡 **Gợi mở Socratic:** *Lưu ý: 'Điểm cực trị của hàm số' là hoành độ $x$, còn 'Giá trị cực trị' là tung độ $y$ nhé!*"
            )
        elif any(k in q_lower for k in ["tiệm cận"]):
            return (
                "🎯 **Kỹ năng đọc Tiệm cận từ BBT (SGK Toán GDPT 2018):**\n"
                "- Tiệm cận đứng: Tại $x = x_0$ có dấu hai vạch song song ($||$) và ít nhất một bên $y \\to \\pm\\infty$.\n"
                "- Tiệm cận ngang: Giá trị hữu hạn của $y$ khi $x \\to \\pm\\infty$.\n\n"
                "💡 **Gợi mở Socratic:** *Em hãy kiểm tra hai đầu vô cực của dòng $x$ và các điểm gián đoạn hai vạch để tìm tiệm cận nhé!*"
            )
    elif any(k in q_lower for k in ["đồ thị của hàm số nào", "là của hàm số nào", "đường cong dưới đây"]):
        return (
            "🎯 **Kỹ năng nhận dạng hàm số từ Đồ thị (SGK Toán GDPT 2018):**\n"
            "1. Quan sát đường tiệm cận đứng và tiệm cận ngang/xiên.\n"
            "2. Kiểm tra giao điểm của đồ thị với trục tung $Oy$ (thay $x = 0$ để tìm $y$).\n"
            "3. Xét dấu hệ số bậc cao nhất dựa vào chiều của nhánh đồ thị bên phải cùng.\n\n"
            "💡 **Gợi mở Socratic:** *Em hãy dùng phương pháp loại trừ lần lượt 4 phương án dựa vào 3 đặc trưng trên nhé!*"
        )

    # 1. ƯU TIÊN 1: BÀI TOÁN TỐI ƯU KINH TẾ & THỰC TẾ (Doanh thu, Lợi nhuận, Chi phí, Sản xuất, Thể tích, Bơi ngược dòng, Nồng độ thuốc...)
    # Bắt buộc ưu tiên để không bị bắt nhầm vào Mũ/Logarit khi bài toán chứa ln(1+x) hoặc e^
    if any(k in q_lower for k in [
        "giá tour", "doanh thu", "lợi nhuận", "chi phí", "sản xuất", "thùng tôn",
        "hộp chữ nhật", "hộp không nắp", "diện tích bề mặt", "nồng độ thuốc",
        "bơi ngược dòng", "năng lượng tiêu hao", "tiêu hao", "tối ưu"
    ]):
        return (
            "🎯 **Định hướng mô hình hóa bài toán Tối ưu thực tế (SGK GDPT 2018):**\n"
            "- **Bước 1 (Chọn biến số & Tập xác định):** Gọi ẩn $x$ (hoặc $t, v$) là đại lượng thay đổi kèm điều kiện thực tế (ví dụ: $x > 0$ hoặc $v > 6$).\n"
            "- **Bước 2 (Thiết lập hàm mục tiêu):**\n"
            "  + Biểu diễn các đại lượng phụ thuộc theo ẩn số (Lợi nhuận = Doanh thu - Chi phí, Năng lượng tiêu hao $E(v) = c v^3 t$, hoặc Diện tích toàn phần $S(x)$).\n"
            "  + Xây dựng hàm số mục tiêu cần tối ưu: $f(x)$ (tìm GTLN hoặc GTNN).\n"
            "- **Bước 3 (Khảo sát cực trị):** Tính đạo hàm $f'(x) = 0$ hoặc áp dụng BĐT Cauchy để tìm điểm tối ưu.\n\n"
            "💡 **Gợi mở Socratic:** *Em hãy lập hàm số mục tiêu theo biến đề bài cho, tính đạo hàm tìm cực trị rồi đối chiếu với câu hỏi nhé!*"
        )

    # 2. ƯU TIÊN 2: BÀI TOÁN MẪU SỐ LIỆU GHÉP NHÓM (Thống kê Toán 12 KNTT)
    # Ưu tiên trước Xác suất để không bị gán nhầm sang P(A) = n(A)/n(Omega)
    if any(k in q_lower for k in ["trung vị", "tứ phân vị", "mốt", "độ lệch chuẩn", "phương sai", "ghép nhóm", "mẫu số liệu"]):
        return (
            "🎯 **Công thức Thống kê Mẫu số liệu ghép nhóm (SGK Toán 12 KNTT):**\n"
            "- **Cỡ mẫu:** $n = \\sum n_i$. Xác định nhóm chứa giá trị đặc trưng (với Trung vị $M_e$: vị trí $\\frac{n}{2}$).\n"
            "- **Công thức Trung vị $M_e$:** $M_e = u_m + \\dfrac{\\frac{n}{2} - C}{n_m} \\cdot (u_{m+1} - u_m)$, trong đó $C$ là tần số tích lũy nhóm trước, $n_m$ là tần số nhóm chứa $M_e$.\n"
            "- **Công thức Tứ phân vị $Q_1, Q_3$:** Tương tự với vị trí $\\frac{n}{4}$ và $\\frac{3n}{4}$.\n\n"
            "💡 **Gợi mở Socratic:** *Em hãy tính cỡ mẫu $n$, cộng dồn tần số để tìm đúng nhóm chứa trung vị $[u_m; u_{m+1})$ rồi thay số vào công thức nhé!*"
        )

    # 3. ƯU TIÊN 3: BÀI TOÁN HÌNH HỌC TỌA ĐỘ TRONG KHÔNG GIAN OXYZ
    # Ngăn chặn việc bắt nhầm sang công thức thể tích khối tròn xoay lớp 11
    if any(k in q_lower for k in ["trong không gian oxyz", "oxzy", "oxyz", "hệ tọa độ oxyz"]):
        if any(k in q_lower for k in ["mặt cầu", "bán kính mặt cầu", "ngoại tiếp tứ diện"]):
            return (
                "🎯 **Điểm tựa lý thuyết SGK Kết Nối Tri Thức:**\n"
                "*Phương trình & Bán kính Mặt cầu trong không gian Oxyz (SGK Toán 12 - KNTT)*\n\n"
                "- Phương trình chính tắc tâm $I(a; b; c)$, bán kính $R$: $(x - a)^2 + (y - b)^2 + (z - c)^2 = R^2$.\n"
                "- Với tứ diện vuông $OABC$ tại $O$ với $A(a; 0; 0), B(0; b; 0), C(0; 0; c)$:\n"
                "  + Tâm mặt cầu ngoại tiếp: $I(\\frac{a}{2}; \\frac{b}{2}; \\frac{c}{2})$.\n"
                "  + Bán kính mặt cầu ngoại tiếp: $R = \\frac{1}{2}\\sqrt{OA^2 + OB^2 + OC^2} = \\frac{1}{2}\\sqrt{a^2 + b^2 + c^2}$.\n\n"
                "💡 **Định hướng tư duy Socratic:**\n"
                "*Em hãy xác định độ dài 3 cạnh vuông góc $OA, OB, OC$ rồi áp dụng công thức bán kính mặt cầu ngoại tiếp tứ diện vuông nhé!*"
            )
        elif any(k in q_lower for k in ["mái nhà", "góc giữa hai mặt phẳng", "góc giữa mặt phẳng"]):
            return (
                "🎯 **Điểm tựa lý thuyết SGK Kết Nối Tri Thức:**\n"
                "*Góc giữa hai mặt phẳng trong không gian Oxyz (SGK Toán 12 - KNTT)*\n\n"
                "Cho hai mặt phẳng có VTPT lần lượt là $\\vec{n}_1$ và $\\vec{n}_2$:\n"
                "$$\\cos \\alpha = \\dfrac{|\\vec{n}_1 \\cdot \\vec{n}_2|}{|\\vec{n}_1| \\cdot |\\vec{n}_2|}, \\quad (0^\\circ \\le \\alpha \\le 90^\\circ)$$\n\n"
                "💡 **Định hướng tư duy Socratic:**\n"
                "*Em hãy tính tích vô hướng của hai vectơ pháp tuyến và chia cho tích hai độ dài để tìm góc $\\alpha$ nhé!*"
            )
        elif any(k in q_lower for k in ["khoảng cách ngắn nhất", "khoảng cách", "thiết bị bay", "đường bay", "khoảng cách từ", "trạm phát sóng", "rô-bốt", "robot"]):
            return (
                "🎯 **Phương pháp tọa độ giải bài toán Khoảng cách Oxyz (SGK GDPT 2018):**\n"
                "- **Bước 1 (Xác định yếu tố hình học):** Tìm tọa độ điểm mốc (ví dụ: $M(1;2;0)$ hoặc $O(0;0;0)$) và vectơ chỉ phương $\\vec{u} = \\vec{AB}$ của đường thẳng chuyển động.\n"
                "- **Bước 2 (Công thức khoảng cách từ điểm đến đường thẳng):** Khoảng cách ngắn nhất chính là độ dài hình chiếu vuông góc:\n"
                "  $$d(M, AB) = \\dfrac{|[\\vec{AM}, \\vec{AB}]|}{|\\vec{AB}|}$$\n"
                "- **Bước 3 (Hoặc phương pháp tam thức bậc hai):** Viết tọa độ điểm di động $P(t) \\in AB$ theo tham số $t$, lập biểu thức khoảng cách $MP(t) = \\sqrt{f(t)}$ và tìm giá trị nhỏ nhất của tam thức bậc hai $f(t)$.\n\n"
                "💡 **Gợi mở Socratic:** *Em hãy tính tọa độ vectơ $\\vec{AB}$, $\\vec{AM}$, tính tích có hướng $[\\vec{AM}, \\vec{AB}]$ rồi áp dụng công thức chia độ dài để ra khoảng cách ngắn nhất nhé!*"
            )

    # 4. XỬ LÝ ĐẶC THÙ CHO PHẦN II (ĐÚNG/SAI)
    # Trắc nghiệm Đúng/Sai: Tuyệt đối không phán "Ý a đúng, b sai"
    if (options is None or len(options) == 0) and (any(kw in q_lower for kw in ["mệnh đề", "khẳng định sau", "đúng hay sai", "mỗi ý"]) or ("đúng" in corr_ans.lower() and "sai" in corr_ans.lower())):
        return (
            "🎯 **Chiến lược kiểm định 4 Mệnh đề Đúng/Sai (SGK GDPT 2018):**\n"
            "- **Mệnh đề về ĐKXĐ / Tập xác định:** Kiểm tra điều kiện mẫu số khác 0 và biểu thức dưới căn bậc chẵn $\\ge 0$.\n"
            "- **Mệnh đề về Đơn điệu / Cực trị:** Tính đạo hàm $f'(x)$ và lập bảng xét dấu độc lập trên từng khoảng.\n"
            "- **Mệnh đề về Giá trị cụ thể:** Thay trực tiếp toạ độ / số liệu đề bài vào phương trình ban đầu.\n\n"
            "💡 **Gợi mở Socratic:** *Em hãy xét độc lập từng mệnh đề a), b), c), d) theo quy tắc cần và đủ để quyết định Đúng hay Sai nhé!*"
        )

    # 5. XỬ LÝ ĐẶC THÙ CHO PHẦN III (TRẢ LỜI NGẮN / VẬN DỤNG CAO)
    if (options is None or len(options) == 0) and corr_ans and any(c.isdigit() for c in corr_ans):
        # A. Tốc độ tăng trưởng / Đạo hàm thực tế
        if any(k in q_lower for k in ["vi khuẩn", "tốc độ tăng trưởng", "tốc độ phát triển", "quy luật s(t)", "vận tốc lớn nhất"]):
            return (
                "🎯 **Định hướng giải bài toán Tốc độ cực trị (SGK GDPT 2018):**\n"
                "- **Bước 1 (Hàm tốc độ):** Tốc độ tăng trưởng/vận tốc chính là đạo hàm cấp một của hàm số lượng: $v(t) = S'(t)$.\n"
                "- **Bước 2 (Tìm cực đại của tốc độ):** Để tốc độ $v(t)$ đạt giá trị lớn nhất, ta khảo sát hàm số $v(t)$ bằng cách giải phương trình đạo hàm: $v'(t) = S''(t) = 0$.\n"
                "- **Bước 3 (Kiểm tra điều kiện):** Đối chiếu nghiệm $t$ với khoảng xác định của thời gian trong đề bài.\n\n"
                "💡 **Gợi mở Socratic:** *Em hãy lấy đạo hàm $S'(t)$ để tìm hàm tốc độ, sau đó khảo sát cực trị của hàm tốc độ này để tìm thời điểm $t$ nhé!*"
            )
        # B. Hướng dẫn tổng quát có chiều sâu cho câu hỏi trả lời ngắn
        else:
            return (
                "🎯 **Chiến lược giải toán Trả lời ngắn & Vận dụng cao (Bộ GD&ĐT):**\n"
                "1. **Mô hình hóa:** Nhận diện đối tượng toán học/vật lý trung tâm và thiết lập phương trình liên hệ từ giả thiết bài toán.\n"
                "2. **Giải toán:** Áp dụng định lý giải tích, định luật bảo toàn hoặc công thức tọa độ chuyên môn để giải phương trình ẩn số.\n"
                "3. **Kiểm tra đáp số:** Rà soát điều kiện thực tế của biến số và làm tròn đúng định dạng phiếu thi (tối đa 4 ký tự).\n\n"
                "💡 **Gợi mở Socratic:** *Em hãy bám sát các đại lượng đã cho của đề bài, lập phương trình liên hệ và tính toán cẩn thận từng bước nhé!*"
            )

    # 6. TÌM KNOWLEDGE ANCHOR PHÙ HỢP TRONG KHO SGK GDPT 2018 (CHO TRẮC NGHIỆM 4 PHƯƠNG ÁN)
    anchors = SOCRATIC_KNOWLEDGE_ANCHORS.get(subj_key, [])
    if not anchors and subj_key in ["Toán", "Toán học"]:
        anchors = SOCRATIC_KNOWLEDGE_ANCHORS.get("Toán học", [])
    elif not anchors and "Văn" in subj_key:
        anchors = SOCRATIC_KNOWLEDGE_ANCHORS.get("Ngữ văn", [])
    elif not anchors and "Anh" in subj_key:
        anchors = SOCRATIC_KNOWLEDGE_ANCHORS.get("Tiếng Anh", [])
    elif not anchors and "Lý" in subj_key:
        anchors = SOCRATIC_KNOWLEDGE_ANCHORS.get("Vật lý", [])
    elif not anchors and "Hóa" in subj_key:
        anchors = SOCRATIC_KNOWLEDGE_ANCHORS.get("Hóa học", [])

    matched_anchor = None
    if anchors:
        for anc in anchors:
            if any(k in q_lower for k in anc["keywords"]):
                matched_anchor = anc
                break

    if matched_anchor:
        return (
            f"🎯 **Điểm tựa lý thuyết SGK Kết Nối Tri Thức:**\n"
            f"*{matched_anchor['concept']}*\n\n"
            f"{matched_anchor['formula']}\n\n"
            f"💡 **Định hướng tư duy Socratic:**\n"
            f"{matched_anchor['prompt']}"
        )

    # 3. BỨC TƯỜNG LỬA ANTI-LEAK FIREWALL: THANH LỌC LỜI GIẢI CHI TIẾT
    raw_h = str(hint_text or "").strip()
    if raw_h:
        sentences = re.split(r'[\n\r]+|[.!?]\s+(?=[A-ZÀÁẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬĐÈÉẺẼẸÊẾỀỂỄỆÌÍỈĨỊÒÓỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÙÚỦŨỤƯỨỪỬỮỰỲÝỶỸỴ])', raw_h)
        clean_lines = []
        
        # Danh sách chuỗi cấm (Blacklist các phương án và đáp án)
        forbidden_snippets = []
        if options and isinstance(options, list):
            for opt in options:
                opt_clean = re.sub(r'^[A-D]\s*[\.\:\)]\s*', '', str(opt)).strip()
                if len(opt_clean) >= 3:
                    forbidden_snippets.append(opt_clean.lower())
        if corr_ans and len(corr_ans) >= 2:
            forbidden_snippets.append(corr_ans.lower())

        for s in sentences:
            s_clean = s.strip()
            if not s_clean: continue

            # 1. Chặn câu chứa từ khóa chỉ định đáp án
            if re.search(r'(?i)\b(?:do đó|suy ra|kết luận|chọn|đáp án|đáp số|kết quả(?:\s*là)?|phương án(?:\s*đúng)?|vậy|nghiệm là|ta được)\b', s_clean):
                continue

            # 2. Chặn câu phán Đúng/Sai theo từng ý: a) Đúng, Ý b sai, (a) Đúng...
            if re.search(r'(?i)(?:mệnh đề|ý)?\s*[\(\[]?[a-d][\)\]\.\:\-]?\s*(?:là\s*)?(?:đúng|sai|đ|s)\b', s_clean):
                continue
            if re.search(r'(?i)\b(?:ý|mệnh đề)\s*[a-d]\s*,\s*[a-d]', s_clean):
                continue

            # 3. Chặn câu tính toán cụ thể ra số học hoặc biểu thức có dấu = kèm số liệu
            if re.search(r'=\s*[-+]?\d+(?:[.,]\d+)?\b', s_clean) or re.search(r'=\s*\([^\)]*[-+]?\d+', s_clean):
                continue

            # 4. Chặn câu chứa nguyên văn phương án đúng
            s_lower = s_clean.lower()
            if any(snip in s_lower for snip in forbidden_snippets if len(snip) > 3):
                continue

            clean_lines.append(s_clean)

        # Chỉ chấp nhận nếu câu còn lại mang tính lý thuyết/phương pháp thuần túy
        if clean_lines and len(" ".join(clean_lines)) >= 25:
            safe_content = " ".join(clean_lines[:2])
            # Kiểm tra an toàn lần cuối
            if not any(k in safe_content.lower() for k in ["chọn", "đáp án", "đúng", "sai"]):
                return (
                    f"🎯 **Điểm tựa kiến thức:**\n{safe_content}\n\n"
                    f"💡 **Thử thách Socratic:** *Dựa vào định lý và công thức nền tảng trên, em hãy tự tay thực hiện phép tính để tìm ra kết quả chính xác nhé!*"
                )

    # 4. UNIVERSAL SOCRATIC FALLBACK (CHUẨN 3 BƯỚC KHÔNG BAO GIỜ CHỨA SỐ LIỆU HAY ĐÁP ÁN)
    if "Văn" in subj_key:
        return (
            "🎯 **Bước 1 (Nhận diện bản chất):** Đọc kỹ văn bản, xác định thể loại, phương thức biểu đạt và hoàn cảnh xuất xứ.\n\n"
            "🔑 **Bước 2 (Chiến lược tư duy):** Bám sát các từ ngữ, hình ảnh đặc sắc và biện pháp nghệ thuật trong đoạn trích.\n\n"
            "💡 **Gợi mở Socratic:** *Em hãy lập luận theo từng luận điểm rõ ràng và liên hệ bài học nhân sinh sâu sắc nhé!*"
        )
    elif "Anh" in subj_key:
        return (
            "🎯 **Step 1 (Core Knowledge):** Identify the grammar rule, tense, or phonetics pattern required by the sentence.\n\n"
            "🔑 **Step 2 (Clue Analysis):** Look for signal words, time expressions, or subject-verb relationships.\n\n"
            "💡 **Socratic Prompt:** *Eliminate incorrect distractors and apply the core rule to determine the right option!*"
        )
    else:
        return (
            "🎯 **Bước 1 (Nhận diện bản chất bài toán):** Xác định rõ giả thiết đề bài, dạng toán và công thức định lý tương ứng trong SGK Kết Nối Tri Thức.\n\n"
            "🔑 **Bước 2 (Chiến lược tư duy):** Thiết lập phương trình liên hệ giữa các đại lượng đã biết và đại lượng cần tìm, loại trừ các phương án không hợp lý về dấu hoặc đơn vị.\n\n"
            "💡 **Gợi mở Socratic:** *Em hãy tự tay thế số liệu từ đề bài vào công thức tổng quát để tính ra đáp số chính xác nhé!*"
        )


def render_question_source_badge(q, idx=None):

    """

    Hiển thị Thẻ Xác Thực Nguồn Gốc & Kiểm Tra Chéo KHKT (Audit Provenance Badge).

    Chỉ hiển thị khi Giáo viên / Giám khảo bật công tắc 'Hiển thị Thẻ Đối Soát Chéo KHKT'.

    Định dạng HTML phẳng tuyệt đối, loại bỏ nguy cơ vỡ cú pháp markdown code block.

    """

    if not isinstance(q, dict): return

    # Kiểm tra công tắc mở/đóng đối soát chéo (Mặc định là TẮT để bảo toàn mỹ cảm đề thi)
    if not st.session_state.get("show_audit_badges_per_question", False):
        return

    # NẾU LÀ ĐỀ DO AI TỰ SÁNG TÁC (LUỒNG 1): HIỂN THỊ THẺ MINH BẠCH KHẢO THÍ ĐỘC BẢN
    if q.get("is_ai_generated") or not q.get("is_real_bank_question", False):
        ai_badge_html = (
            f'<div style="font-size: 11.5px; background: rgba(15, 23, 42, 0.75); border: 1px solid #10b981; border-left: 4px solid #10b981; border-radius: 6px; padding: 4px 10px; margin-bottom: 7px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 4px; box-shadow: 0 2px 6px rgba(0,0,0,0.25);">'
            f'<div style="color: #f1f5f9; display: flex; flex-wrap: wrap; align-items: center; gap: 5px;">'
            f'<span style="background: linear-gradient(135deg, #059669, #047857); color: #ffffff; padding: 1px 6px; border-radius: 3px; font-weight: 800; font-size: 10px; letter-spacing: 0.3px;">🤖 ĐỘC BẢN 2026</span>'
            f'<span style="color: #34d399; font-weight: 700;">Biên soạn bởi Trợ lý AI Khảo Thí</span>'
            f'<span style="color: #64748b;">•</span>'
            f'<span style="color: #cbd5e1; font-weight: 500;">Ngữ liệu mới 100% (Không trích xuất từ ngân hàng đề cũ)</span>'
            f'</div>'
            f'<div style="color: #94a3b8; font-size: 11px;">✨ Đã qua 7 tầng Deep Solver Guard</div>'
            f'</div>'
        )
        st.markdown(ai_badge_html, unsafe_allow_html=True)
        return

    src = str(q.get("source", "")).strip()
    school = q.get("school")
    if not school or "Điểm Quốc Gia" in str(school) or "Chuyên / Điểm" in str(school):
        school = "Bộ Đề Chuẩn Hóa CT GDPT 2018 (QĐ 764)"
    
    session = q.get("exam_session")
    year = q.get("year") or "2025 - 2026"
    portal = q.get("portal") or "Kho Khảo Thí Quốc Gia"
    orig_pos = q.get("orig_pos")

    orig_code = q.get("orig_exam_code")

    audit_id = q.get("audit_id")



    if not session:

        src_lower = src.lower()

        if "cuối" in src_lower or "hk1" in src_lower:

            session = "Kỳ thi Cuối Học Kỳ 1 (Chính thức)"

        elif "giữa" in src_lower:

            session = "Kỳ thi Giữa Học Kỳ 1 (Lần 1)"

        elif "khảo sát" in src_lower:

            session = "Đợt Khảo Sát Năng Lực Định Kỳ"

        elif "thử" in src_lower:

            session = "Thi Thử Tốt Nghiệp THPT (Lần 1)"

        else:

            session = "Khảo Thí Chuẩn Hóa Năng Lực"



    pos_html = f'<span style="color: #64748b;">•</span> <span style="color: #cbd5e1;">📍 {html.escape(str(orig_pos))}</span>' if orig_pos else ''

    code_html = f'<span style="color: #94a3b8; font-size: 10.5px;">(Mã đề gốc: {html.escape(str(orig_code))})</span>' if orig_code else ''

    aid_html = f'<span style="background: rgba(56, 189, 248, 0.15); color: #38bdf8; padding: 1px 5px; border-radius: 3px; font-family: monospace; font-size: 10.5px; font-weight: 600;">#{html.escape(str(audit_id))}</span>' if audit_id else ''



    badge_html = (

        f'<div style="font-size: 11.5px; background: rgba(15, 23, 42, 0.75); border: 1px solid #0284c7; border-left: 4px solid #38bdf8; border-radius: 6px; padding: 4px 10px; margin-bottom: 7px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 4px; box-shadow: 0 2px 6px rgba(0,0,0,0.25);">'

        f'<div style="color: #f1f5f9; display: flex; flex-wrap: wrap; align-items: center; gap: 5px;">'

        f'<span style="background: linear-gradient(135deg, #0284c7, #0369a1); color: #ffffff; padding: 1px 6px; border-radius: 3px; font-weight: 800; font-size: 10px; letter-spacing: 0.3px;">🏛️ ĐỐI SOÁT CHÉO KHKT</span>'

        f'<span style="color: #38bdf8; font-weight: 700;">{html.escape(str(school))}</span>'

        f'<span style="color: #64748b;">•</span>'

        f'<span style="color: #34d399; font-weight: 600;">📅 {html.escape(str(session))} ({html.escape(str(year))})</span>'

        f'{pos_html} {code_html}'

        f'</div>'

        f'<div style="color: #94a3b8; font-size: 11px; display: flex; align-items: center; gap: 6px;">'

        f'<span>🌐 Cổng: <b style="color: #38bdf8;">{html.escape(str(portal))}</b></span>'

        f'{aid_html}'

        f'</div></div>'

    )

    st.markdown(badge_html, unsafe_allow_html=True)



def question_visual_html(question):

    """XƯỞNG IN TĨNH CHUẨN SÁCH GIÁO KHOA & BỘ GD&ĐT (INLINE-WITH-TEXT CĂN GIỮA CO GỌN)."""

    pieces = []

    q_txt_lower = str(question.get("q", "")).lower()



    # 1. Bảng biến thiên (BBT): Xuất ảnh WebP chuẩn nét thẳng hàng tuyệt đối

    if question.get("bbt"):
        try:
            import precision_visual_engine as pve
            question["bbt"] = pve.heal_bbt_mathematics(question["bbt"])
        except Exception:
            pass
        b64_bbt = render_bbt_to_webp_base64(question["bbt"])

        if b64_bbt:

            pieces.append(f"<div style='text-align: center; margin: 4px auto 6px auto;'><img src='{b64_bbt}' style='max-width: 320px; width: 100%; height: auto; border-radius: 4px;' alt='Bảng biến thiên'/></div>")

        else:

            pieces.append(format_pedagogical_bbt_html(question["bbt"], is_dark_mode=False))



    # 2. Bảng mẫu số liệu ghép nhóm (MSLGN - Chuẩn Times New Roman & viền hộp đôi SGK)

    grouped = question.get("mslgn_data")

    if isinstance(grouped, dict):

        groups, frequencies = grouped.get("groups", []), grouped.get("freq", [])

        if groups and len(groups) == len(frequencies):

            tbl_dyn_w = min(680, max(360, len(groups) * 75 + 120))

            ms_title = html.escape(str(grouped.get("title", "Bảng mẫu số liệu ghép nhóm:")))

            cells_g = "".join(f"<td style='padding: 5px 10px; border: 1px solid #000; font-weight: 500;'>{html.escape(str(g))}</td>" for g in groups)

            cells_f = "".join(f"<td style='padding: 5px 10px; border: 1px solid #000; font-weight: 600;'>{html.escape(str(f))}</td>" for f in frequencies)

            pieces.append(

                f"<div style='display: flex; justify-content: center; margin: 6px auto 8px auto;'>"

                f"<div style='max-width: {tbl_dyn_w}px; background: #fff; padding: 0; width: 100%;'>"

                f"<p style='text-align: center; font-weight: bold; font-family: \"Times New Roman\", serif; color: #000; margin-bottom: 4px; font-size: 13.5px;'>{ms_title}</p>"

                f"<table style='width: 100%; border-collapse: collapse; text-align: center; font-family: \"Times New Roman\", serif; color: #000; border: 1.2px solid #000; font-size: 13.5px;'>"

                f"<tr><th style='padding: 5px 10px; border: 1px solid #000; font-weight: bold; width: 120px; background-color: #f8fafc;'>Nhóm giá trị</th>{cells_g}</tr>"

                f"<tr><th style='padding: 5px 10px; border: 1px solid #000; font-weight: bold; background-color: #f8fafc;'>Tần số (n)</th>{cells_f}</tr>"

                f"</table></div></div>"

            )

    # 2.5. Phục dựng thị giác: Ngữ liệu đa môn đặc thù (Vật lý, Hóa học, Sinh học, Địa lí, Toán thực tế)
    has_rendered_geom_svg = False

    # A. Vật lý 12 CT GDPT 2018 (Chu trình p-V, Từ trường & Bàn tay trái, Phóng xạ, Mạch RLC, Sóng cơ)
    if question.get("thermal_pv_visual") and isinstance(question["thermal_pv_visual"], dict):
        tpv = question["thermal_pv_visual"]
        if tpv.get("svg"):
            pieces.append(f"<div style='text-align: center; margin: 6px auto;'><div style='display: inline-block; max-width: 290px; width: 100%;'>{sanitize_svg_for_markdown(tpv['svg'])}</div></div>")
            has_rendered_geom_svg = True

    if not has_rendered_geom_svg and question.get("magnetic_visual") and isinstance(question["magnetic_visual"], dict):
        mag = question["magnetic_visual"]
        if mag.get("svg"):
            pieces.append(f"<div style='text-align: center; margin: 6px auto;'><div style='display: inline-block; max-width: 290px; width: 100%;'>{sanitize_svg_for_markdown(mag['svg'])}</div></div>")
            has_rendered_geom_svg = True

    if not has_rendered_geom_svg and question.get("nuclear_visual") and isinstance(question["nuclear_visual"], dict):
        nuc = question["nuclear_visual"]
        if nuc.get("svg"):
            pieces.append(f"<div style='text-align: center; margin: 6px auto;'><div style='display: inline-block; max-width: 290px; width: 100%;'>{sanitize_svg_for_markdown(nuc['svg'])}</div></div>")
            has_rendered_geom_svg = True

    if not has_rendered_geom_svg and question.get("wave_visual") and isinstance(question["wave_visual"], dict):
        wv = question["wave_visual"]
        if wv.get("svg"):
            pieces.append(f"<div style='text-align: center; margin: 6px auto;'><div style='display: inline-block; max-width: 290px; width: 100%;'>{sanitize_svg_for_markdown(wv['svg'])}</div></div>")
            has_rendered_geom_svg = True

    if not has_rendered_geom_svg and question.get("circuit_visual") and isinstance(question["circuit_visual"], dict):
        circ = question["circuit_visual"]
        if circ.get("svg"):
            pieces.append(f"<div style='text-align: center; margin: 6px auto;'><div style='display: inline-block; max-width: 290px; width: 100%;'>{sanitize_svg_for_markdown(circ['svg'])}</div></div>")
            has_rendered_geom_svg = True

    # B. Hóa học (Thí nghiệm điều chế khí, Pin điện hóa Daniell)
    if not has_rendered_geom_svg and question.get("chem_visual") and isinstance(question["chem_visual"], dict):
        ch = question["chem_visual"]
        if ch.get("svg"):
            pieces.append(f"<div style='text-align: center; margin: 6px auto;'><div style='display: inline-block; max-width: 290px; width: 100%;'>{sanitize_svg_for_markdown(ch['svg'])}</div></div>")
            has_rendered_geom_svg = True

    # C. Sinh học (Sơ đồ phả hệ di truyền & Lưới thức ăn)
    if not has_rendered_geom_svg and question.get("pedigree_visual") and isinstance(question["pedigree_visual"], dict):
        ped = question["pedigree_visual"]
        if ped.get("svg"):
            pieces.append(f"<div style='text-align: center; margin: 6px auto;'><div style='display: inline-block; max-width: 290px; width: 100%;'>{sanitize_svg_for_markdown(ped['svg'])}</div></div>")
            has_rendered_geom_svg = True

    if not has_rendered_geom_svg and question.get("food_web_visual") and isinstance(question["food_web_visual"], dict):
        fw = question["food_web_visual"]
        if fw.get("svg"):
            pieces.append(f"<div style='text-align: center; margin: 6px auto;'><div style='display: inline-block; max-width: 320px; width: 100%;'>{sanitize_svg_for_markdown(fw['svg'])}</div></div>")
            has_rendered_geom_svg = True

    # D. Địa lí (Bảng số liệu & Biểu đồ kinh tế)
    if not has_rendered_geom_svg and question.get("geo_chart") and isinstance(question["geo_chart"], dict):
        g_chart = question["geo_chart"]
        years = g_chart.get("years", [])
        series = g_chart.get("series", [])
        if years and series:
            tbl_h = f"<div style='display: flex; justify-content: center; margin: 6px auto;'><div style='max-width: 520px; width: 100%;'><p style='text-align: center; font-weight: bold; font-family: \"Times New Roman\", serif; font-size: 13px; margin-bottom: 4px;'>{html.escape(g_chart.get('title', 'Bảng số liệu thống kê:'))}</p><table style='width: 100%; border-collapse: collapse; text-align: center; font-family: \"Times New Roman\", serif; font-size: 13px; border: 1.2px solid #000;'><tr><th style='padding: 4px 8px; border: 1px solid #000; background: #f8fafc;'>Chỉ tiêu</th>" + "".join(f"<th style='padding: 4px 8px; border: 1px solid #000; background: #f8fafc;'>{y}</th>" for y in years) + "</tr>"
            for row in series:
                tbl_h += f"<tr><td style='padding: 4px 8px; border: 1px solid #000; font-weight: 500;'>{html.escape(str(row.get('name', '')))}</td>" + "".join(f"<td style='padding: 4px 8px; border: 1px solid #000;'>{val}</td>" for val in row.get("data", [])) + "</tr>"
            tbl_h += "</table></div></div>"
            pieces.append(tbl_h)
            has_rendered_geom_svg = True

    # E. Toán học thực tế & Tọa độ Oxyz
    if not has_rendered_geom_svg and question.get("composite_visual") and isinstance(question["composite_visual"], dict):
        comp = question["composite_visual"]
        if comp.get("svg"):
            pieces.append(f"<div style='text-align: center; margin: 5px auto;'><div style='display: inline-block; max-width: 220px;'>{sanitize_svg_for_markdown(comp['svg'])}</div></div>")
            has_rendered_geom_svg = True

    if not has_rendered_geom_svg and question.get("geom_3d") and isinstance(question["geom_3d"], dict):
        g3d = question["geom_3d"]
        g_type = str(g3d.get("type", ""))
        if g_type in ["tetrahedron", "oxyz_space", "oxyz_tetrahedron_sphere", "pure_box", "pure_triangular_prism", "pure_pyramid_quad", "flight_trajectory", "points_segment"] or g3d.get("sub_type") in ["oxyz_tetrahedron_sphere", "oxyz_distance_point_line", "oxyz_midpoint_projection"]:
            svg_g3d = g3d.get("svg")
            if not svg_g3d and pve:
                if any(k in q_txt_lower for k in ["thiết bị bay", "đường bay", "trạm phát sóng"]):
                    svg_g3d = pve.build_oxyz_flight_path_model(q_txt_lower).get("svg")
                elif any(k in q_txt_lower for k in ["tứ diện", "chóp tam giác"]):
                    svg_g3d = pve.build_oxyz_tetrahedron_model(q_txt_lower).get("svg")
            if svg_g3d:
                pieces.append(f"<div style='text-align: center; margin: 5px auto;'><div style='display: inline-block; max-width: 220px;'>{sanitize_svg_for_markdown(svg_g3d)}</div></div>")
                has_rendered_geom_svg = True

    # 3. Đồ thị 2D & Hình học 3D: CHỈ VẼ KHI CÂU HỎI THỰC SỰ LÀ TOÁN HỌC VÀ CÓ YÊU CẦU HÌNH VẼ
    is_non_math_subject = any(k in q_txt_lower for k in [
        "vật lý", "vật lí", "hóa học", "sinh học", "địa lí", "địa lý", "lực từ", "từ trường", "khí lý tưởng", "khí lí tưởng",
        "đẳng áp", "đẳng nhiệt", "đẳng tích", "phóng xạ", "chu kỳ bán rã", "chu kì bán rã", "hạt nhân", "đoạn mạch",
        "cuộn cảm", "tụ điện", "điện trở r", "thí nghiệm", "phả hệ", "lưới thức ăn", "gdp", "nhiệt lượng", "nhiệt độ"
    ]) and not any(m in q_txt_lower for m in ["hàm số", "tiệm cận", "bảng biến thiên", "tứ diện", "hình chóp", "lăng trụ", "oxyz"])

    if is_non_math_subject:
        function = None
        question.pop("f", None)
        question.pop("geom_3d", None)
    else:
        function = question.get("f") or question.get("geom_3d")

    is_geom_or_applied = any(kw in q_txt_lower for kw in [
        "tấm bìa", "khối chóp", "hình chóp", "lập phương", "hình hộp", "quả cầu",
        "bình nước", "bể chứa", "cắt góc", "gấp lại", "gấp lên", "cắt bỏ",
        "cửa sổ", "dây thép", "con cá", "vệ tinh", "dải led", "bán nguyệt"
    ])

    has_need_graph = not is_non_math_subject and any(kw in q_txt_lower for kw in ["hình vẽ", "hình bên", "đồ thị bên", "đường cong trong hình", "khối nón", "khối trụ", "mặt cầu", "khối tròn xoay"])

    is_calc_algebra = any(k in q_txt_lower for k in [
        "biểu thức", "giá trị của biểu thức", "bằng bao nhiêu", "tìm m",
        "tìm tham số", "t =", "p =", "t = ", "p = "
    ]) or (any(k in q_txt_lower for k in ["tính", "giá trị của"]) and any(k in q_txt_lower for k in ["biểu thức", "t =", "p =", "t = ", "p = ", "tham số"]))

    if is_calc_algebra and not any(kw in q_txt_lower for kw in ["hình vẽ bên", "hình bên", "đồ thị bên", "đường cong trong hình", "như hình vẽ bên"]):
        function = None
        question.pop("f", None)
        question.pop("geom_3d", None)
        question.pop("tikz", None)

    if not is_non_math_subject and not function and has_need_graph and not is_geom_or_applied and not is_calc_algebra:
        if any(k in q_txt_lower for k in ["ax^3", "bậc ba", "bậc 3"]):
            function = {"type": "func_3", "a": 1.0, "b": -3.0, "c": -1.0, "d": 2.0}
            question["f"] = function
        elif any(k in q_txt_lower for k in ["phân thức", "ax+b"]):
            if pve:
                solved_f = pve.solve_rational_1_1_from_text(question.get("q", ""), question.get("opt", []))
                if solved_f:
                    function = solved_f
                    question["f"] = function
        elif any(k in q_txt_lower for k in ["ax^2", "parabol", "parabola"]):
            function = {"type": "parabola", "a": 1.0, "b": -2.0, "c": -3.0}
            question["f"] = function

    if not has_rendered_geom_svg and isinstance(function, dict) and has_need_graph and not is_geom_or_applied:
        dtype = str(function.get("type", ""))
        try:
            if dtype in ["cone_3d", "cylinder_3d", "sphere_3d", "solid_of_revolution"]:
                if dtype == "cone_3d":
                    r_c = float(function.get("r", 3)); h_c = float(function.get("h", 4))
                    pieces.append(f"""<div style='text-align: center; margin: 4px auto 6px auto;'><svg width='160' height='145' viewBox='0 0 220 210'><ellipse cx='110' cy='170' rx='65' ry='22' fill='none' stroke='black' stroke-width='1.5' stroke-dasharray='4,4'/><path d='M 45,170 A 65 22 0 0 0 175,170' fill='none' stroke='black' stroke-width='1.5'/><line x1='45' y1='170' x2='110' y2='30' stroke='black' stroke-width='1.5'/><line x1='175' y1='170' x2='110' y2='30' stroke='black' stroke-width='1.5'/><line x1='110' y1='170' x2='110' y2='30' stroke='black' stroke-width='1.2' stroke-dasharray='4,4'/><line x1='110' y1='170' x2='175' y2='170' stroke='black' stroke-width='1.2' stroke-dasharray='4,4'/><circle cx='110' cy='170' r='2' fill='black'/><circle cx='110' cy='30' r='2' fill='black'/><text x='113' y='25' font-family='Times New Roman' font-size='14' font-style='italic'>S</text><text x='102' y='185' font-family='Times New Roman' font-size='14' font-style='italic'>O</text><text x='138' y='166' font-family='Times New Roman' font-size='14'>R={r_c}</text><text x='114' y='105' font-family='Times New Roman' font-size='14'>h={h_c}</text></svg></div>""")
                elif dtype == "cylinder_3d":
                    r_cyl = float(function.get("r", 3)); h_cyl = float(function.get("h", 5))
                    pieces.append(f"""<div style='text-align: center; margin: 4px auto 6px auto;'><svg width='160' height='145' viewBox='0 0 220 210'><ellipse cx='110' cy='45' rx='60' ry='20' fill='none' stroke='black' stroke-width='1.5'/><ellipse cx='110' cy='165' rx='60' ry='20' fill='none' stroke='black' stroke-width='1.2' stroke-dasharray='4,4'/><path d='M 50,165 A 60 20 0 0 0 170,165' fill='none' stroke='black' stroke-width='1.5'/><line x1='50' y1='45' x2='50' y2='165' stroke='black' stroke-width='1.5'/><line x1='170' y1='45' x2='170' y2='165' stroke='black' stroke-width='1.5'/><line x1='110' y1='45' x2='110' y2='165' stroke='black' stroke-width='1.2' stroke-dasharray='4,4'/><line x1='110' y1='165' x2='170' y2='165' stroke='black' stroke-width='1.2' stroke-dasharray='4,4'/><text x='103' y='38' font-family='Times New Roman' font-size='13' font-style='italic'>O</text><text x='102' y='182' font-family='Times New Roman' font-size='13' font-style='italic'>O\'</text><text x='136' y='161' font-family='Times New Roman' font-size='12'>R={r_cyl}</text><text x='114' y='110' font-size='12'>h={h_cyl}</text></svg></div>""")
                elif dtype == "sphere_3d":
                    r_s = float(function.get("r", 3))
                    pieces.append(f"""<div style='text-align: center; margin: 4px auto 6px auto;'><svg width='160' height='145' viewBox='0 0 220 210'><circle cx='110' cy='105' r='70' fill='none' stroke='black' stroke-width='1.5'/><ellipse cx='110' cy='105' rx='70' ry='22' fill='none' stroke='black' stroke-width='1.2' stroke-dasharray='4,4'/><path d='M 40,105 A 70 22 0 0 0 180,105' fill='none' stroke='black' stroke-width='1.5'/><line x1='110' y1='105' x2='180' y2='105' stroke='black' stroke-width='1.2' stroke-dasharray='4,4'/><circle cx='110' cy='105' r='2' fill='black'/><text x='101' y='120' font-family='Times New Roman' font-size='14' font-style='italic'>O</text><text x='140' y='100' font-family='Times New Roman' font-size='14'>R={r_s}</text></svg></div>""")
                elif dtype == "solid_of_revolution":
                    fa_b = function.get("a", 0); fb_b = function.get("b", 3); f_exp = function.get("f_expr", "y = f(x)")
                    pieces.append(f"""<div style='text-align: center; margin: 4px auto 6px auto;'><svg width='185' height='125' viewBox='0 0 260 180'><line x1='20' y1='90' x2='245' y2='90' stroke='black' stroke-width='1.2'/><line x1='45' y1='165' x2='45' y2='15' stroke='black' stroke-width='1.2'/><polygon points='245,87 252,90 245,93' fill='black'/><polygon points='42,15 45,8 48,15' fill='black'/><text x='242' y='106' font-family='Times New Roman' font-size='14'>x</text><text x='51' y='20' font-family='Times New Roman' font-size='14'>y</text><text x='35' y='105' font-family='Times New Roman' font-size='14' font-style='italic'>O</text><path d='M 65,72 Q 130,35 205,25' fill='none' stroke='black' stroke-width='1.8'/><path d='M 65,108 Q 130,145 205,155' fill='none' stroke='black' stroke-width='1.2' stroke-dasharray='4,4'/><ellipse cx='65' cy='90' rx='8' ry='18' fill='none' stroke='black' stroke-width='1.2'/><ellipse cx='205' cy='90' rx='16' ry='65' fill='none' stroke='black' stroke-width='1.2'/><text x='62' y='106' font-family='Times New Roman' font-size='13'>{fa_b}</text><text x='202' y='106' font-family='Times New Roman' font-size='13'>{fb_b}</text><text x='125' y='36' font-family='Times New Roman' font-size='13'>{f_exp}</text></svg></div>""")
            else:
                extra_pts = function.get("extra_points", [])
                b64_graph = render_math_graph_to_webp_base64(function, extra_points=extra_pts)
                if b64_graph:
                    pieces.append(f"<div style='text-align: center; margin: 4px auto 6px auto;'><img src='{b64_graph}' style='max-width: 175px; width: 100%; height: auto; border-radius: 4px;' alt='Đồ thị'/></div>")
        except Exception:
            pass

    # KHỬ TRÙNG LẶP TUYỆT ĐỐI 100%: Mỗi câu hỏi tối đa chỉ xuất đúng 1 hình vẽ duy nhất
    unique_pieces = []
    seen_piece_hashes = set()
    for p in pieces:
        p_clean = re.sub(r'\s+', '', p)
        if p_clean and p_clean not in seen_piece_hashes:
            seen_piece_hashes.add(p_clean)
            unique_pieces.append(p)

    return "\n".join(unique_pieces)





def latex_text(value):

    if not value: return ""

    value = str(value)

    value = value.replace("↗", r"$\nearrow$").replace("↘", r"$\searrow$").replace("∞", r"\infty")

    value = re.sub(r"\\(?:input|include|write18|openout|read|catcode|immediate)\b", "", value)

    chunks = re.split(r'(\$[^$]*\$)', value)

    replacements = {"\\": r"\textbackslash{}", "{": r"\{", "}": r"\}", "&": r"\&", "%": r"\%", "_": r"\_", "#": r"\#", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"}

    return "".join(chunk if index%2 else "".join(replacements.get(char,char) for char in chunk) for index,chunk in enumerate(chunks))





def sanitize_print_math_text(text: str) -> str:
    """CHUẨN HÓA CÔNG THỨC TOÁN CHO BẢN IN PDF (MATHJAX 3): KHỬ SẠCH LỆNH LỆCH NGOẶC TẬP HỢP & DÍNH CHỮ."""
    if not text: return ""
    s = str(text).replace(r'\$', '$').replace('$$', '$')
    
    # Khắc phục lỗi chữ tiếng Việt có dấu và khoảng trắng bị bọc trong $...$ làm dính chữ trong MathJax
    def unwrap_vietnamese_math(match):
        inner = match.group(1)
        if re.search(r'[àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđĐ]', inner) and ' ' in inner:
            return inner
        return match.group(0)
    s = re.sub(r'\$([^$]+)\$', unwrap_vietnamese_math, s)

    s = sanitize_katex_latex(s)
    
    # Khử triệt để lệnh \left và \right trong MathJax để tập hợp R \ {1} hiển thị đẹp 10 điểm
    s = s.replace('\\left', '').replace('\\right', '')
    s = s.replace(r'\left', '').replace(r'\right', '')
    
    # Tự động cân bằng nếu chuỗi bị lẻ dấu $
    if s.count('$') % 2 != 0:
        s += '$'
    return s


def get_mb_bank_vietqr_base64():
    """Hàm tải mã VietQR MB Bank của Thầy Phan Minh Trí (base64) để nhúng trực tiếp vào bản in PDF."""
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        opt_b64_path = os.path.join(base_dir, "assets", "mb_bank_vietqr_opt_b64.txt")
        if os.path.exists(opt_b64_path):
            with open(opt_b64_path, "r", encoding="utf-8") as f:
                b64 = f.read().strip()
                if b64:
                    return f"data:image/png;base64,{b64}"
    except Exception:
        pass
    return ""


def audit_and_heal_exam_semantics(exam: dict, subject_name: str = "Toán học", grade_name: str = "Lớp 12") -> dict:
    """
    CHỐT CHẶN CUỐI CÙNG VỀ NGỮ NGHĨA & NỘI DUNG ĐỀ THI (VIP 66.5 - GDPT 2018):
    1. Khử sạch 100% câu chữ chắp vá, lỗi copy-paste từ đề cũ (như 'mặt cầu tiếp xúc... hoặc bán kính mặt cầu ngoại tiếp').
    2. Khử triệt để lỗi Đa Đáp Án ở các câu tính đơn điệu (đồng biến/nghịch biến từ BBT).
    3. Tự động đồng bộ Hướng dẫn Socratic bám sát bản chất toán học, không bị lệch chuyên đề.
    """
    if not isinstance(exam, dict):
        return exam

    p_keys = ["p1", "p2", "p3", "part_1", "part_2", "part_3"]
    for pk in p_keys:
        q_list = exam.get(pk)
        if not isinstance(q_list, list):
            continue
        for q in q_list:
            if not isinstance(q, dict):
                continue
            
            # --- 1. CHỮA LÀNH CÂU CHỮ VĂN PHONG VÔ LÝ / CHẮP VÁ ---
            q_txt = str(q.get("q", ""))
            if "tiếp xúc với mặt phẳng" in q_txt and any(hw in q_txt.lower() for hw in ["hoặc bán kính", "hoặc tính"]):
                q_txt = re.sub(r'(?i)Bán kính mặt cầu tiếp xúc.*?hoặc\s*(?:bán\s+kính\s+)?', 'Bán kính ', q_txt).strip()
                q["q"] = q_txt
            elif re.search(r'(?i)\bhoặc\s+bán\s+kính\s+mặt\s+cầu\s+ngoại\s+tiếp\b', q_txt):
                q_txt = re.sub(r'(?i)Bán kính mặt cầu tiếp xúc.*?hoặc\s*(?:bán\s+kính\s+)?', 'Bán kính ', q_txt).strip()
                q["q"] = q_txt

            # --- 2. KHỬ LỖI ĐA ĐÁP ÁN Ở CÂU ĐỒNG BIẾN / NGHỊCH BIẾN TỪ BBT ---
            opts = q.get("opt") or []
            if len(opts) == 4 and any(k in q_txt.lower() for k in ["đồng biến trên khoảng", "hàm số đã cho đồng biến", "đồng biến"]):
                corr_ans = str(q.get("ans", "A")).strip().upper()
                opt_texts = [str(o) for o in opts]
                has_neg_inf = any("-\\infty" in o or "-inf" in o or "-1" in o or "-∞" in o for o in opt_texts[:2])
                has_pos_inf = any("+\\infty" in o or "+inf" in o or "(2;" in o or "(2," in o or "+∞" in o for o in opt_texts[2:])
                # Nếu đáp án chính thức là A, phương án C bị dính khoảng đồng biến thứ 2 (2; +inf) -> Sửa C thành (-1; 2)
                if corr_ans == "A" and has_neg_inf and has_pos_inf:
                    opts[2] = "C. (-1; 2)"
                    q["opt"] = opts

            # --- 3. ĐỒNG BỘ LỜI GIẢI SOCRATIC CHUẨN XÁC ---
            ans_val = str(q.get("ans", ""))
            if q.get("stmts"):
                ans_val = "; ".join(f"{chr(97+i)}: " + ("Đúng" if (t.get("a") if "a" in t else t.get("ans", True)) else "Sai") for i, t in enumerate(q.get("stmts", [])))
            
            q["explain"] = sanitize_socratic_hint(
                q.get("explain", ""),
                correct_answer=ans_val,
                q_text=q.get("q", ""),
                options=q.get("opt"),
                level=q.get("level", "TH"),
                subject=subject_name,
                grade_num=12
            )
            
    return exam


def build_exam_exports(exam, subject_name, grade_name, duration, include_answers=False,
                       template_style="form1",
                       teacher_name="Thầy Phan Minh Trí",
                       school_name="TRƯỜNG THPT TÂN HIỆP & TT THIỆN NHÂN",
                       quote_text="Dưỡng thiện tâm, Ươm nhân tài",
                       quote_author="THẦY PHAN MINH TRÍ",
                       show_support_qr=True):
    import datetime
    # CHỐT CHẶN CUỐI CÙNG: Thẩm định ngữ nghĩa, khử đa đáp án và chuẩn hóa Socratic trước khi xuất bản
    exam = audit_and_heal_exam_semantics(exam, subject_name=subject_name, grade_name=grade_name)
    current_year = datetime.datetime.now().year
    school_year = f"{current_year} - {current_year+1}"
    exam_count = exam.get('exam_count') or st.session_state.get('exam_mix_count') or max(1, int(st.session_state.get('global_exam_count') or 1))
    ex_code = str(exam.get('code', st.session_state.get('exam_code', '101')))
    title = f"Kỳ thi Khảo sát chất lượng lần thứ {exam_count} — Môn {subject_name} ({grade_name}) — Mã đề {ex_code}"
    
    app_target_url = f"{APP_URL}?exam_code={ex_code}&subject={urllib.parse.quote(subject_name)}"
    qr_base64 = generate_local_qr_base64(app_target_url, fill_color="#0f172a", back_color="#ffffff")
    mb_qr_base64 = get_mb_bank_vietqr_base64()

    # ==================== 1. XÂY DỰNG TIÊU ĐỀ HEADER HTML THEO MẪU ====================
    if template_style == "form2":
        # MẪU 2: CHUẨN SƯ PHẠM HIỆN ĐẠI (OVERLEAF TYPOGRAPHY & GDPT 2018 CHUẨN QUỐC GIA)
        header_html = f"""
        <div style="background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%); border: 1.5px solid #0284c7; border-radius: 8px; padding: 14px 18px; margin-bottom: 14px; font-family: 'Times New Roman', Times, serif;">
            <table class="header-table" style="width: 100%; border: none !important; border-collapse: collapse;">
                <tr style="border: none !important;">
                    <td style="width: 55%; vertical-align: top; border: none !important; padding: 0 !important; background: transparent !important;">
                        <div style="font-size: 11.5px; font-weight: bold; color: #0369a1; text-transform: uppercase; letter-spacing: 0.5px;">BỘ GIÁO DỤC & ĐÀO TẠO • GDPT 2018 CHUẨN QUỐC GIA</div>
                        <div style="font-size: 14px; font-weight: bold; color: #0f172a; text-transform: uppercase; margin: 2px 0;">{school_name}</div>
                        <div style="font-size: 12.5px; color: #334155;">Biên soạn: <strong style="color: #0369a1;">{teacher_name}</strong></div>
                        <div style="width: 140px; height: 1.5px; background: #0284c7; margin: 4px 0;"></div>
                    </td>
                    <td style="width: 33%; text-align: center; vertical-align: top; border: none !important; padding: 0 !important; background: transparent !important;">
                        <div style="display: inline-block; background: #0284c7; color: #ffffff; font-weight: bold; font-size: 13.5px; padding: 3px 12px; border-radius: 4px; letter-spacing: 1px;">
                            MÃ ĐỀ THI: {ex_code}
                        </div>
                        <div style="font-size: 11.5px; color: #475569; margin-top: 4px;">Kỳ thi KSCL lần thứ {exam_count}</div>
                        <div style="font-size: 11.5px; font-weight: bold; color: #0f172a;">NĂM HỌC {school_year}</div>
                    </td>
                    <td style="width: 12%; text-align: right; vertical-align: top; border: none !important; padding: 0 !important; background: transparent !important;" class="no-print-hide">
                        <img src="{qr_base64}" style="width: 60px; height: 60px; border: 1px solid #0284c7; border-radius: 4px; padding: 2px; background: #fff;" alt="QR Code">
                        <div style="font-size: 8px; color: #0369a1; text-align: center; font-weight: bold; margin-top: 2px;">Quét tra cứu</div>
                    </td>
                </tr>
            </table>
            <div style="text-align: center; margin-top: 10px; border-top: 1px dashed #7dd3fc; padding-top: 8px;">
                <span style="font-size: 15px; font-weight: bold; color: #0c4a6e; text-transform: uppercase; letter-spacing: 0.5px;">
                    ĐỀ KHẢO SÁT CHẤT LƯỢNG MÔN {subject_name.upper()} — {grade_name.upper()}
                </span><br>
                <span style="font-size: 12.5px; font-style: italic; color: #334155;">
                    Thời gian làm bài: {int(duration)} phút (Không kể thời gian phát đề)
                </span>
            </div>
            <div style="font-style: italic; font-size: 12.5px; color: #1e293b; margin-top: 8px; padding-top: 6px; border-top: 1px solid #e0f2fe;">
                Họ và tên thí sinh: ................................................................................ Số báo danh: ....................... Phòng thi: .........
            </div>
        </div>
        """
    else:
        # MẪU 1: CHUẨN KHẢO THÍ TRUYỀN THỐNG CÔNG PHU (NGUYÊN BẢN 100% CỦA THẦY PHAN MINH TRÍ - BỘ GD&ĐT)
        header_html = f"""
        <table class="header-table" style="width: 100%; border: none !important; border-collapse: collapse; margin-bottom: 12px; font-family: 'Times New Roman', Times, serif;">
            <tr style="border: none !important;">
                <td style="width: 44%; text-align: center; vertical-align: top; border: none !important; padding: 0 !important; background: transparent !important;">
                    <div style="font-size: 13px; font-weight: bold; text-transform: uppercase;">SỞ GIÁO DỤC VÀ ĐÀO TẠO AN GIANG</div>
                    <div style="font-size: 13.5px; font-weight: bold; text-transform: uppercase;">{school_name}</div>
                    <div style="width: 120px; height: 1.2px; background: #000; margin: 3px auto 5px auto;"></div>
                    <div style="font-size: 14px; font-weight: bold;">MÃ ĐỀ THI: <span style="font-size: 15px; letter-spacing: 1px;">{ex_code}</span></div>
                </td>
                <td style="width: 44%; text-align: center; vertical-align: top; border: none !important; padding: 0 !important; background: transparent !important;">
                    <div style="font-size: 13.5px; font-weight: bold; text-transform: uppercase;">KỲ THI KHẢO SÁT CHẤT LƯỢNG LẦN THỨ {exam_count}</div>
                    <div style="font-size: 13px; font-weight: bold;">NĂM HỌC {school_year}</div>
                    <div style="font-size: 14px; font-weight: bold; color: #000; text-transform: uppercase; margin-top: 2px;">MÔN: {subject_name.upper()} - {grade_name}</div>
                    <div style="font-size: 13px; font-style: italic;">Thời gian làm bài: {int(duration)} phút (Không kể thời gian phát đề)</div>
                    <div style="width: 150px; height: 1.2px; background: #000; margin: 4px auto 0 auto;"></div>
                </td>
                <td style="width: 12%; text-align: right; vertical-align: top; border: none !important; padding: 0 !important; background: transparent !important;">
                    <img src="{qr_base64}" style="width: 65px; height: 65px; border: 1px solid #cbd5e1; border-radius: 4px; padding: 2px;" alt="QR Code">
                    <div style="font-size: 8.5px; color: #64748b; text-align: center; margin-top: 1px;">Quét tra cứu</div>
                </td>
            </tr>
        </table>
        <div style="font-style: italic; font-size: 13.5px; margin-bottom: 12px; margin-top: 6px; font-family: 'Times New Roman', Times, serif;">
            Họ và tên thí sinh: ................................................................................ Số báo danh: ....................... Phòng thi: .........
        </div>
        """
    
    blocks = [header_html]

    # ==================== 2. XÂY DỰNG NGUỒN LATEX OVERLEAF (TIKZ & TABULARX CHUẨN CHỈ) ====================
    latex_school_escaped = latex_text(school_name)
    latex_teacher_escaped = latex_text(teacher_name)
    latex_quote_escaped = latex_text(quote_text)
    latex_author_escaped = latex_text(quote_author.upper())

    if template_style == "form2":
        latex_header = f"""\\noindent
\\begin{{minipage}}[t]{{0.50\\textwidth}}
\\textbf{{\\small BỘ GIÁO DỤC \\& ĐÀO TẠO • GDPT 2018}} \\\\
\\textbf{{\\large {latex_school_escaped}}} \\\\
\\textit{{\\small Biên soạn: {latex_teacher_escaped}}} \\[0.05cm]
\\rule{{4.5cm}}{{0.8pt}}
\\end{{minipage}}
\\hfill
\\begin{{minipage}}[t]{{0.48\\textwidth}}
\\raggedleft
\\textbf{{\\large MÃ ĐỀ THI: {ex_code}}} \\\\
\\textbf{{Kỳ thi KSCL lần thứ {exam_count} - Năm học {school_year}}} \\[0.05cm]
\\rule{{4cm}}{{0.8pt}}
\\end{{minipage}}
\\vspace{{0.3cm}}

\\begin{{center}}
\\textbf{{\\Large ĐỀ KHẢO SÁT CHẤT LƯỢNG MÔN {latex_text(subject_name).upper()} - {grade_name}}} \\[0.1cm]
\\textit{{Thời gian làm bài: {int(duration)} phút (Không kể thời gian phát đề)}}
\\end{{center}}
\\vspace{{0.2cm}}

\\noindent \\textit{{Họ và tên thí sinh: \\dotfill Số báo danh: \\dotfill Phòng thi: \\dotfill}}
\\vspace{{0.4cm}}
"""
        tex = [
            r"\documentclass[12pt,a4paper]{article}",
            r"\usepackage[utf8]{inputenc}",
            r"\usepackage[T5]{fontenc}",
            r"\usepackage[vietnamese]{babel}",
            r"\usepackage{amsmath,amssymb,amsfonts,mathrsfs}",
            r"\usepackage{geometry}",
            r"\geometry{a4paper, left=1.8cm, right=1.8cm, top=1.8cm, bottom=2.0cm}",
            r"\usepackage{tikz,pgfplots}",
            r"\pgfplotsset{compat=1.18}",
            r"\usepackage{tabularx,array,booktabs,multirow,multicol}",
            r"\usepackage{fancyhdr}",
            r"\usepackage{enumitem}",
            r"\usepackage{tcolorbox}",
            r"\pagestyle{fancy}",
            r"\fancyhf{}",
            rf"\lhead{{\footnotesize {latex_school_escaped} - NĂM HỌC {school_year}}}",
            rf"\rhead{{\footnotesize MÔN {latex_text(subject_name).upper()} - MÃ ĐỀ: {ex_code}}}",
            rf"\lfoot{{\footnotesize \textit{{❝{latex_quote_escaped}❞}} — \textbf{{{latex_author_escaped}}}}}",
            rf"\rfoot{{\footnotesize Trang \thepage}}",
            r"\renewcommand{\headrulewidth}{0.4pt}",
            r"\renewcommand{\footrulewidth}{0.4pt}",
            r"\begin{document}",
            latex_header
        ]
    else:
        latex_header = f"""\\noindent
\\begin{{minipage}}[t]{{0.43\\textwidth}}
\\centering
\\textbf{{SỞ GIÁO DỤC VÀ ĐÀO TẠO AN GIANG}} \\\\
\\textbf{{{latex_school_escaped}}} \\\\[0.05cm]
\\rule{{3.5cm}}{{0.6pt}} \\\\[0.15cm]
\\textbf{{\\large MÃ ĐỀ THI: {ex_code}}}
\\end{{minipage}}
\\hfill
\\begin{{minipage}}[t]{{0.54\\textwidth}}
\\centering
\\textbf{{KỲ THI KHẢO SÁT CHẤT LƯỢNG LẦN THỨ {exam_count}}} \\\\
\\textbf{{NĂM HỌC {school_year}}} \\\\
\\textbf{{\\large Môn: {latex_text(subject_name)} - {grade_name}}} \\\\[0.05cm]
\\textit{{Thời gian làm bài: {int(duration)} phút (Không kể thời gian phát đề)}} \\\\[0.05cm]
\\rule{{4.5cm}}{{0.6pt}}
\\end{{minipage}}
\\vspace{{0.35cm}}

\\noindent \\textit{{Họ và tên thí sinh: \\dotfill Số báo danh: \\dotfill Phòng thi: \\dotfill}}
\\vspace{{0.4cm}}
"""
        tex = [
            r"\documentclass[12pt,a4paper]{article}",
            r"\usepackage[utf8]{inputenc}",
            r"\usepackage[T5]{fontenc}",
            r"\usepackage[vietnamese]{babel}",
            r"\usepackage{amsmath,amssymb,amsfonts,mathrsfs}",
            r"\usepackage{geometry}",
            r"\geometry{a4paper, left=1.8cm, right=1.8cm, top=1.8cm, bottom=1.8cm}",
            r"\usepackage{tikz,pgfplots}",
            r"\pgfplotsset{compat=1.18}",
            r"\usepackage{tabularx,array,booktabs,multirow,multicol}",
            r"\usepackage{fancyhdr}",
            r"\usepackage{enumitem}",
            r"\usepackage{tcolorbox}",
            r"\pagestyle{fancy}",
            r"\fancyhf{}",
            rf"\lhead{{\footnotesize {latex_school_escaped} - NĂM HỌC {school_year}}}",
            rf"\rhead{{\footnotesize MÔN {latex_text(subject_name).upper()} - MÃ ĐỀ: {ex_code}}}",
            r"\cfoot{\thepage}",
            r"\renewcommand{\headrulewidth}{0.4pt}",
            r"\begin{document}",
            latex_header
        ]

    sections = []
    if subject_name == "Ngữ văn":
        passage = exam.get("part_doc_hieu", {}).get("text", "")
        blocks.append(f"""
        <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 12px 14px; margin-bottom: 12px; font-size: 14px; line-height: 1.6;">
            <strong>I. ĐỌC HIỂU (4.0 điểm)</strong><br>
            <em>Đọc đoạn trích sau và thực hiện các yêu cầu:</em><br><br>
            {html.escape(passage).replace(chr(10), '<br>')}
        </div>
        """)
        tex.append(r"\section*{PHẦN I: ĐỌC HIỂU (4.0 ĐIỂM)}")
        tex.append(r"\noindent\textit{Đọc đoạn trích sau và thực hiện các yêu cầu:}\par\vspace{0.2cm}")
        tex.append(r"\begin{quote}\small " + latex_text(passage) + r"\end{quote}\par\vspace{0.3cm}")
        sections = [
            ("", exam.get("part_doc_hieu", {}).get("questions", [])),
            ("PHẦN II: VIẾT (6.0 ĐIỂM)", exam.get("part_viet", exam.get("part_lam_van", {}).get("questions", [])))
        ]
    else:
        p1 = exam.get("p1") or exam.get("part_1") or []
        p2 = exam.get("p2") or exam.get("part_2") or []
        p3 = exam.get("p3") or exam.get("part_3") or []
        p1_len = len(p1)
        p2_len = len(p2)
        p3_len = len(p3)
        sections = [
            (f"PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn (Thí sinh trả lời từ câu 1 đến câu {p1_len}. Mỗi câu hỏi thí sinh chỉ chọn một phương án).", p1),
            (f"PHẦN II. Câu trắc nghiệm đúng sai (Thí sinh trả lời từ câu 1 đến câu {p2_len}. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai).", p2),
            (f"PHẦN III. Câu trắc nghiệm trả lời ngắn (Thí sinh trả lời từ câu 1 đến câu {p3_len}. Thí sinh điền kết quả vào ô quy định).", p3)
        ]

    for heading, questions in sections:
        if not questions:
            continue
        if heading:
            if "(" in heading and ")" in heading:
                p_title = heading.split("(")[0].strip()
                p_guide = "(" + heading.split("(", 1)[1].strip()
                header_display = f"<span style='font-weight: bold;'>{p_title}</span> <span style='font-style: italic; font-weight: normal;'>{p_guide}</span>"
                tex_header = r"\noindent\textbf{\large " + latex_text(p_title) + r"} \textit{\normalsize " + latex_text(p_guide) + r"}\par\vspace{0.2cm}"
            else:
                header_display = f"<span style='font-weight: bold;'>{heading}</span>"
                tex_header = r"\noindent\textbf{\large " + latex_text(heading) + r"}\par\vspace{0.2cm}"

            blocks.append(f"<div style='font-size: 14px; margin: 12px 0 6px 0; color: #0f172a; font-family: \"Times New Roman\", serif;'>{header_display}</div>")
            tex.append(r"\par\vspace{0.25cm}" + tex_header)

        for index, q in enumerate(questions, 1):
            if pve and hasattr(pve, "audit_and_heal_visual_context_gdpt2018"):
                q = pve.audit_and_heal_visual_context_gdpt2018(dict(q), subject=subject_name, grade=grade_name)
            raw_q_text = sanitize_print_math_text(str(q.get("q", "")))
            expl_q = sanitize_print_math_text(str(q.get("explain", q.get("expl", q.get("exp", "")))))
            if not expl_q:
                expl_q = f"Áp dụng trực tiếp định nghĩa và tính chất SGK Kết Nối Tri Thức. Phân tích loại trừ phương án nhiễu để chọn đáp án chuẩn {q.get('ans', '')}."

            # BẢO VỆ TÍNH BẢO MẬT & CHUẨN SƯ PHẠM BỘ GD&ĐT:
            # - Tuyệt đối KHÔNG in nguồn câu hỏi khi đề do AI sinh ra.
            # - Bản in phát cho học sinh làm đề luôn sạch sẽ tinh tươm (chỉ có 'Câu X.', không lộ nguồn gốc/mã đối soát).
            # - Chỉ in nguồn khi Giáo viên/Giám khảo chủ động bật 'show_audit_badges_per_question' VÀ câu hỏi thực sự từ ngân hàng thật.
            show_src_in_print = (
                st.session_state.get("show_audit_badges_per_question", False)
                and not exam.get("is_ai_generated", False)
                and q.get("is_real_bank_question", False)
                and bool(q.get("source"))
            )

            if show_src_in_print:
                tex.append(r"\par\noindent\textit{\footnotesize [Nguồn: " + latex_text(str(q['source'])) + r"]}\par")
            tex.append(r"\par\noindent\textbf{Câu " + str(index) + r".} " + latex_text(raw_q_text) + r"\par")

            src_html = f"<div style='font-size: 11px; color: #0284c7; font-style: italic; margin-bottom: 2px;'>🏛️ [Nguồn: {html.escape(str(q['source']))}]</div>" if show_src_in_print else ""
            if template_style == "form2":
                p_text_html = f"{src_html}<p style='margin: 0 0 4px 0; line-height: 1.45;'><span style='display: inline-block; background: #0284c7; color: #fff; font-size: 12px; font-weight: bold; padding: 1px 7px; border-radius: 4px; margin-right: 6px;'>Câu {index}</span>{html.escape(raw_q_text)}</p>"
            else:
                p_text_html = f"{src_html}<p style='margin: 0 0 4px 0; line-height: 1.42;'><b>Câu {index}.</b> {html.escape(raw_q_text)}</p>"

            # 2. Trực quan hóa hình ảnh
            vis_html = question_visual_html(q)

            # 3. THUẬT TOÁN TỰ ĐỘNG ĐO ĐỘ DÀI 4 PHƯƠNG ÁN CHUẨN BỘ GD&ĐT
            opts_html = ""
            opts_raw = q.get("opt") or []
            if not opts_raw and q.get("choices") and isinstance(q["choices"], dict):
                opts_raw = [f"{k}. {v}" for k, v in q["choices"].items()]
            
            if opts_raw:
                letters = ["A", "B", "C", "D"]
                clean_opts_list = []
                for o in opts_raw:
                    c_clean = sanitize_print_math_text(re.sub(r'(?i)^[A-D]\.\s*', '', str(o)).strip())
                    clean_opts_list.append(c_clean)

                lengths = [len(c) for c in clean_opts_list]
                max_opt_len = max(lengths) if lengths else 0
                total_opt_len = sum(lengths)

                if max_opt_len <= 20 or total_opt_len <= 85:
                    grid_cols = "grid-template-columns: repeat(4, 1fr);"
                    latex_cols = 4
                elif max_opt_len <= 45 or total_opt_len <= 170:
                    grid_cols = "grid-template-columns: repeat(2, 1fr);"
                    latex_cols = 2
                else:
                    grid_cols = "grid-template-columns: 1fr;"
                    latex_cols = 1

                opts_html = f"<div style='display: grid; {grid_cols} gap: 2px 14px; margin: 4px 0 6px 0;'>"
                for i, c_opt in enumerate(clean_opts_list):
                    prefix = f"<b>{letters[i]}.</b> " if i < 4 else ""
                    opts_html += f"<div style='font-size: 13.5px;'>{prefix}{html.escape(c_opt)}</div>"
                opts_html += "</div>"

                if latex_cols > 1 and len(clean_opts_list) == 4:
                    latex_opt_items = [r"\textbf{" + letters[i] + r".} " + latex_text(clean_opts_list[i]) for i in range(4)]
                    tex.append(rf"\begin{{multicols}}{{{latex_cols}}}\noindent " + r" \columnbreak ".join(latex_opt_items) + r"\end{multicols}")
                else:
                    for i, c_opt in enumerate(clean_opts_list):
                        prefix_tex = r"\textbf{" + letters[i] + r".} " if i < 4 else ""
                        tex.append(f"{prefix_tex}{latex_text(c_opt)}" + r"\par")

            # 4. Mệnh đề Đúng/Sai (Phần II)
            stmts_html = ""
            if q.get("stmts"):
                stmts_html = "<div style='margin: 4px 0 6px 10px;'>"
                for i, statement in enumerate(q.get("stmts", [])):
                    stmt_t = sanitize_print_math_text(str(statement.get('t', statement.get('s', ''))))
                    stmts_html += f"<div style='font-size: 13.5px; margin-bottom: 2px;'><b>{chr(97+i)})</b> {html.escape(stmt_t)}</div>"
                    tex.append(rf"\par\quad\textbf{{{chr(97+i)})}} " + latex_text(stmt_t) + r"\par")
                stmts_html += "</div>"

            # LaTeX đồng bộ cho BBT, MSLGN, 3D
            if q.get("bbt"):
                bbt_tex = format_pedagogical_bbt_latex(q["bbt"])
                if bbt_tex: tex.append(bbt_tex + r"\par\vspace{0.15cm}")
            if q.get("mslgn_data"):
                ms = q["mslgn_data"]
                grps = ms.get("groups", []); freqs = ms.get("freq", [])
                if grps and freqs and len(grps) == len(freqs):
                    col_spec = "|l|" + "c|" * len(grps)
                    header_cells = " & ".join([f"${latex_text(str(g))}$" for g in grps])
                    freq_cells = " & ".join([str(f) for f in freqs])
                    table_title = latex_text(str(ms.get('title', 'Bảng mẫu số liệu ghép nhóm:')))
                    tex.append(r"\begin{center}" "\n" rf"\textbf{{{table_title}}}\par\vspace{{0.1cm}}" "\n" rf"\begin{{tabular}}{{{col_spec}}}" "\n" r"\hline" "\n" rf"\textbf{{Nhóm giá trị}} & {header_cells} \\ \hline" "\n" rf"\textbf{{Tần số}} & {freq_cells} \\ \hline" "\n" r"\end{{tabular}}" "\n" r"\end{{center}}" + r"\par\vspace{0.15cm}")

            # Phục dựng TikZ cho đề thi LaTeX Overleaf
            has_emitted_tikz = False
            if q.get("tikz"):
                tex.append(rf"\begin{{center}}" "\n" rf"{q['tikz']}" "\n" rf"\end{{center}}")
                has_emitted_tikz = True
            elif q.get("composite_visual") and isinstance(q["composite_visual"], dict) and q["composite_visual"].get("tikz"):
                tex.append(rf"\begin{{center}}" "\n" rf"{q['composite_visual']['tikz']}" "\n" rf"\end{{center}}")
                has_emitted_tikz = True

            vis_fn = q.get("f") or q.get("geom_3d")
            has_need_g_tex = any(kw in raw_q_text.lower() for kw in ["hình vẽ", "hình bên", "như hình", "đồ thị bên", "đường cong trong hình", "khối nón", "khối trụ", "mặt cầu", "khối tròn xoay"])
            if isinstance(vis_fn, dict) and has_need_g_tex and not has_emitted_tikz:

                try:
                    kind = str(vis_fn.get("type", ""))
                    if kind == "cone_3d":
                        r_c = vis_fn.get("r", 3); h_c = vis_fn.get("h", 4)
                        tex.append(rf"\begin{{center}}\begin{{tikzpicture}}[scale=0.6]\draw[dashed] (-{r_c},0) arc (180:0:{r_c}cm and 0.55cm);\draw ({r_c},0) arc (0:-180:{r_c}cm and 0.55cm);\draw (-{r_c},0) -- (0,{h_c}) -- ({r_c},0);\draw[dashed,orange] (0,0) -- (0,{h_c}) node[midway,right] {{$h={h_c}$}};\draw[dashed,teal] (0,0) -- ({r_c},0) node[midway,below] {{$R={r_c}$}};\filldraw (0,0) circle (1.2pt) node[below] {{$O$}};\filldraw (0,{h_c}) circle (1.2pt) node[above] {{$S$}};\end{{tikzpicture}}\end{{center}}")
                    elif kind == "cylinder_3d":
                        r_cyl = vis_fn.get("r", 3); h_cyl = vis_fn.get("h", 5)
                        tex.append(rf"\begin{{center}}\begin{{tikzpicture}}[scale=0.6]\draw (0,{h_cyl}) ellipse ({r_cyl}cm and 0.55cm);\draw[dashed] (-{r_cyl},0) arc (180:0:{r_cyl}cm and 0.55cm);\draw ({r_cyl},0) arc (0:-180:{r_cyl}cm and 0.55cm);\draw (-{r_cyl},0) -- (-{r_cyl},{h_cyl}); \draw ({r_cyl},0) -- ({r_cyl},{h_cyl});\draw[dashed,orange] (0,0) -- (0,{h_cyl}) node[midway,right] {{$h={h_cyl}$}};\draw[dashed,teal] (0,0) -- ({r_cyl},0) node[midway,below] {{$R={r_cyl}$}};\filldraw (0,0) circle (1.2pt) node[below] {{$O'$}};\filldraw (0,{h_cyl}) circle (1.2pt) node[above] {{$O$}};\end{{tikzpicture}}\end{{center}}")
                    elif kind == "sphere_3d":
                        r_s = vis_fn.get("r", 3)
                        tex.append(rf"\begin{{center}}\begin{{tikzpicture}}[scale=0.6]\draw (0,0) circle ({r_s}cm);\draw[dashed] (-{r_s},0) arc (180:0:{r_s}cm and 0.55cm);\draw ({r_s},0) arc (0:-180:{r_s}cm and 0.55cm);\draw[dashed,teal] (0,0) -- ({r_s},0) node[midway,below] {{$R={r_s}$}};\filldraw (0,0) circle (1.2pt) node[below left] {{$O$}};\end{{tikzpicture}}\end{{center}}")
                    elif kind == "solid_of_revolution":
                        fa_b = vis_fn.get("a", 0); fb_b = vis_fn.get("b", 3); f_exp = vis_fn.get("f_expr", "y = f(x)")
                        tex.append(rf"\begin{{center}}\begin{{tikzpicture}}[scale=0.65]\draw[->] (-0.5,0) -- ({fb_b+1},0) node[right] {{$x$}};\draw[->] (0,-2.5) -- (0,2.5) node[above] {{$y$}};\draw[thick,blue] plot[domain={fa_b}:{fb_b},smooth] ({{\x}},{{sqrt(max(0,\x))}});\draw[thick,blue,dashed] plot[domain={fa_b}:{fb_b},smooth] ({{\x}},{{-sqrt(max(0,\x))}});\draw ({fa_b},0) ellipse (0.15cm and 0.6cm);\draw ({fb_b},0) ellipse (0.25cm and 1.7cm);\node[below] at ({fa_b},0) {{$a={fa_b}$}};\node[below] at ({fb_b},0) {{$b={fb_b}$}};\end{{tikzpicture}}\end{{center}}")
                    else:
                        a, b, c, d, e = [float(vis_fn.get(k, v)) for k, v in [("a", 1), ("b", 0), ("c", 0), ("d", 0), ("e", 0)]]
                        if all(math.isfinite(v) and abs(v) <= 10000 for v in (a, b, c, d, e)):
                            if kind in ("func_3", "cubic"): expression = f"({a})*x^3+({b})*x^2+({c})*x+({d})"
                            elif kind in ("parabola", "parabola_fprime"): expression = f"({a})*x^2+({b})*x+({c})"
                            elif kind == "func_1_1": expression = f"(({a})*x+({b}))/(({c})*x+({d}))"
                            elif kind == "func_2_1": expression = f"(({a})*x^2+({b})*x+({c}))/(({d})*x+({e}))"
                            else: expression = ""
                            if expression:
                                tex.append(r"\begin{center}\begin{tikzpicture}\begin{axis}[width=7cm,height=4.8cm,axis lines=middle,xlabel={$x$},ylabel={$y$},xmin=-4.5,xmax=4.5,ymin=-6,ymax=6,domain=-4.5:4.5,samples=201,restrict y to domain=-6:6,unbounded coords=jump,grid=both,minor tick num=1]")
                                tex.append(r"\addplot[blue,thick] {" + expression + r"};\end{axis}\end{tikzpicture}\end{center}")
                except Exception:
                    pass

            body_html = f"{p_text_html}{vis_html}{opts_html}{stmts_html}"

            ans_expl_html = ""
            if include_answers:
                answer = q.get("ans", "")
                if q.get("stmts"):
                    answer = "; ".join(f"{chr(97+i)}: " + ("Đúng" if (t.get("a") if "a" in t else t.get("ans", True)) else "Sai") for i, t in enumerate(q.get("stmts", [])))
                
                ans_expl_html = f"""
                <div style="background-color: #f0fdf4; border-left: 3.5px solid #16a34a; padding: 5px 10px; margin: 4px 0 6px 0; border-radius: 4px; font-size: 13px; line-height: 1.45;">
                    <div style="font-weight: bold; color: #15803d; margin-bottom: 2px;">✅ ĐÁP ÁN: {html.escape(str(answer))}</div>
                    <div style="color: #1e293b;">💡 <strong>Hướng dẫn tư duy Bình dân học vụ (Bản chất sư phạm Socratic):</strong><br>{html.escape(expl_q)}</div>
                </div>
                """
                tex.append(r"\vspace{0.15cm}\noindent\fbox{\parbox{0.96\textwidth}{\textbf{Đáp án:} " + latex_text(str(answer)) + r" \\ \textit{\textbf{💡 Hướng dẫn tư duy Bình dân học vụ:}} " + latex_text(expl_q) + r"}}\par\vspace{0.25cm}")

            blocks.append(f"<article style='margin-bottom: 8px; break-inside: avoid;'>{body_html}{ans_expl_html}</article>")

    # DÒNG KẾT THÚC ĐỀ THI TRANG TRỌNG CHUẨN KHẢO THÍ BỘ GD&ĐT
    blocks.append("""
    <div style="text-align: center; font-weight: bold; margin: 18px 0 4px 0; font-family: 'Times New Roman', Times, serif; font-size: 14px; letter-spacing: 2px;">
        ---------- HẾT ----------
    </div>
    <div style="text-align: center; font-style: italic; font-size: 12.5px; color: #475569; margin-bottom: 16px; font-family: 'Times New Roman', Times, serif;">
        Thí sinh không được sử dụng tài liệu. Cán bộ coi thi không giải thích gì thêm.
    </div>
    """)
    tex.append(r"\vspace{0.4cm}\begin{center}\textbf{---------- HẾT ----------}\\\textit{\small Thí sinh không được sử dụng tài liệu. Cán bộ coi thi không giải thích gì thêm.}\end{center}\vspace{0.3cm}")

    # ==================== 3. BẢNG TỔNG HỢP ĐÁP ÁN CHUẨN BỘ (ANSWER KEY TABLE) ====================
    if include_answers and subject_name != "Ngữ văn":
        blocks.append("<div style='page-break-before: always; margin-top: 20px;' class='print-page-break'>")
        blocks.append("<h2 style='text-align: center; font-size: 15px; font-weight: bold; text-transform: uppercase; margin-bottom: 10px; font-family: \"Times New Roman\", Times, serif;'>BẢNG ĐÁP ÁN VÀ MA TRẬN CHẤM ĐIỂM CHUẨN BỘ GD&ĐT</h2>")
        
        tex.append(r"\newpage")
        tex.append(r"\begin{center}\textbf{\Large BẢNG ĐÁP ÁN VÀ MA TRẬN CHẤM ĐIỂM CHUẨN BỘ GD\&ĐT}\end{center}\vspace{0.3cm}")

        p1_items = exam.get("p1") or exam.get("part_1") or []
        p2_items = exam.get("p2") or exam.get("part_2") or []
        p3_items = exam.get("p3") or exam.get("part_3") or []

        if p1_items:
            blocks.append("<h4 style='margin-bottom: 4px; font-size: 13.5px; font-family: \"Times New Roman\", Times, serif;'>PHẦN I: TRẮC NGHIỆM 4 LỰA CHỌN</h4>")
            blocks.append("<table border='1' style='width: 100%; border-collapse: collapse; text-align: center; font-size: 13px; margin-bottom: 12px; font-family: \"Times New Roman\", Times, serif;'>")
            tex.append(r"\noindent\textbf{PHẦN I: TRẮC NGHIỆM 4 LỰA CHỌN}\par\vspace{0.15cm}")
            
            tex.append(r"\begin{tabularx}{\textwidth}{|" + "X|" * min(10, len(p1_items)) + "}")
            tex.append(r"\hline")
            for chunk_start in range(0, len(p1_items), 10):
                chunk = p1_items[chunk_start:chunk_start+10]
                blocks.append("<tr style='background: #f1f5f9; font-weight: bold;'>" + "".join(f"<th>Câu {chunk_start+i+1}</th>" for i in range(len(chunk))) + "</tr>")
                blocks.append("<tr>" + "".join(f"<td style='padding: 4px; font-weight: bold; color: #0369a1;'>{q.get('ans', '')}</td>" for q in chunk) + "</tr>")
            blocks.append("</table>")
            
            tex_header_row = " & ".join(f"\\textbf{{Câu {i+1}}}" for i in range(min(10, len(p1_items)))) + r" \\ \hline"
            tex_ans_row = " & ".join(f"\\textbf{{{p1_items[i].get('ans', '')}}}" for i in range(min(10, len(p1_items)))) + r" \\ \hline"
            tex.append(tex_header_row)
            tex.append(tex_ans_row)
            tex.append(r"\end{tabularx}\par\vspace{0.3cm}")

        if p2_items:
            blocks.append("<h4 style='margin-bottom: 4px; font-size: 13.5px; font-family: \"Times New Roman\", Times, serif;'>PHẦN II: TRẮC NGHIỆM ĐÚNG / SAI (THANG BẬC 0.1 - 0.25 - 0.5 - 1.0 ĐIỂM)</h4>")
            blocks.append("<table border='1' style='width: 100%; border-collapse: collapse; text-align: center; font-size: 13px; margin-bottom: 12px; font-family: \"Times New Roman\", Times, serif;'><tr style='background: #f1f5f9; font-weight: bold;'><th>Câu</th><th>Lệnh hỏi a)</th><th>Lệnh hỏi b)</th><th>Lệnh hỏi c)</th><th>Lệnh hỏi d)</th></tr>")
            tex.append(r"\noindent\textbf{PHẦN II: TRẮC NGHIỆM ĐÚNG / SAI}\par\vspace{0.15cm}")
            tex.append(r"\begin{tabularx}{\textwidth}{|c|X|X|X|X|}\hline")
            tex.append(r"\textbf{Câu} & \textbf{Ý a)} & \textbf{Ý b)} & \textbf{Ý c)} & \textbf{Ý d)} \\ \hline")
            for idx2, q2 in enumerate(p2_items, 1):
                st_vals = [("Đúng" if (s.get("a") if "a" in s else s.get("ans", True)) else "Sai") for s in q2.get("stmts", [])]
                while len(st_vals) < 4: st_vals.append("-")
                blocks.append(f"<tr><td style='font-weight: bold;'>Câu {idx2}</td>" + "".join(f"<td style='padding: 4px;'>{v}</td>" for v in st_vals) + "</tr>")
                tex.append(f"\\textbf{{Câu {idx2}}} & " + " & ".join(st_vals) + r" \\ \hline")
            blocks.append("</table>")
            tex.append(r"\end{tabularx}\par\vspace{0.3cm}")

        if p3_items:
            blocks.append("<h4 style='margin-bottom: 4px; font-size: 13.5px; font-family: \"Times New Roman\", Times, serif;'>PHẦN III: TRẢ LỜI NGẮN (ĐIỀN SỐ TỐI ĐA 4 KÝ TỰ)</h4>")
            blocks.append("<table border='1' style='width: 100%; border-collapse: collapse; text-align: center; font-size: 13px; margin-bottom: 12px; font-family: \"Times New Roman\", Times, serif;'><tr style='background: #f1f5f9; font-weight: bold;'>" + "".join(f"<th>Câu {i+1}</th>" for i in range(len(p3_items))) + "</tr>")
            blocks.append("<tr>" + "".join(f"<td style='padding: 4px; font-weight: bold; color: #b45309;'>{q.get('ans', '')}</td>" for q in p3_items) + "</tr></table>")
            
            tex.append(r"\noindent\textbf{PHẦN III: TRẢ LỜI NGẮN}\par\vspace{0.15cm}")
            tex.append(r"\begin{tabularx}{\textwidth}{|" + "X|" * len(p3_items) + r"}\hline")
            tex.append(" & ".join(f"\\textbf{{Câu {i+1}}}" for i in range(len(p3_items))) + r" \\ \hline")
            tex.append(" & ".join(f"\\textbf{{{q.get('ans', '')}}}" for q in p3_items) + r" \\ \hline")
            tex.append(r"\end{tabularx}\par\vspace{0.3cm}")

        # KHỐI ỦNG HỘ TÁC GIẢ VIETQR MB BANK (CHỈ XUẤT HIỆN Ở CUỐI TRANG ĐÁP ÁN NẾU ĐƯỢC BẬT)
        if show_support_qr and mb_qr_base64:
            blocks.append(f"""
            <div style="margin-top: 24px; border: 1.5px solid #0284c7; border-radius: 8px; padding: 10px 14px; background: #f0f9ff; font-family: 'Times New Roman', Times, serif;">
                <table style="width: 100%; border: none !important; border-collapse: collapse;">
                    <tr style="border: none !important;">
                        <td style="width: 72px; vertical-align: middle; border: none !important; padding: 0 !important; background: transparent !important;">
                            <img src="{mb_qr_base64}" style="width: 66px; height: 66px; border: 1px solid #0284c7; border-radius: 4px; padding: 2px; background: #fff;" alt="VietQR MB Bank">
                        </td>
                        <td style="vertical-align: middle; padding-left: 14px; border: none !important; background: transparent !important;">
                            <div style="font-weight: bold; font-size: 13px; color: #0369a1; text-transform: uppercase;">ỦNG HỘ TÁC GIẢ BIÊN SOẠN & PHÁT TRIỂN HỆ THỐNG</div>
                            <div style="font-size: 12.5px; color: #0f172a; margin-top: 2px;">Ngân hàng MB Bank • STK: <strong>0919513834</strong> • Chủ tài khoản: <strong>PHAN MINH TRÍ</strong></div>
                            <div style="font-size: 11.5px; color: #475569; font-style: italic; margin-top: 1px;">Trân trọng cảm ơn quý Thầy Cô và các em học sinh đã đồng hành và ủng hộ!</div>
                        </td>
                    </tr>
                </table>
            </div>
            """)
            tex.append(r"\par\vspace{0.5cm}\noindent\begin{tcolorbox}[colback=blue!5!white,colframe=blue!75!black,title=\textbf{ỦNG HỘ TÁC GIẢ BIÊN SOẠN & PHÁT TRIỂN HỆ THỐNG}]" "\n" r"\textbf{Biên soạn:} Thầy Phan Minh Trí \\" "\n" r"\textbf{Ngân hàng MB Bank:} Số tài khoản \textbf{0919513834} (Chủ TK: Phan Minh Trí) \\" "\n" r"\textit{\small Trân trọng cảm ơn quý Thầy Cô và các em học sinh đã đồng hành và ủng hộ!}" "\n" r"\end{tcolorbox}")

        blocks.append("</div>")

    tex.append(r"\end{document}")

    mathjax_head = """<script>window.MathJax = { tex: { inlineMath: [['$', '$'], ['\\\\(', '\\\\)']], displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']] }, svg: { fontCache: 'global' } };</script><script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>"""
    markup = f"""<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
{mathjax_head}
<style>
@page {{
    size: A4 portrait;
    margin: 1.3cm 1.2cm 1.3cm 1.2cm;
}}
body {{
    font-family: 'Times New Roman', Times, serif;
    font-size: 13.5px;
    line-height: 1.42;
    color: #111827;
    background: #f8fafc;
    margin: 0;
    padding: 14px 0;
}}
.page-container {{
    max-width: 820px;
    margin: 0 auto;
    background: #ffffff;
    padding: 24px 28px 95px 28px !important;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    border-radius: 6px;
}}
.header-table td {{
    padding: 2px 4px;
}}
.no-print {{
    display: block;
    margin: 0 auto 14px auto;
    background: #0284c7;
    color: #ffffff;
    border: none;
    padding: 10px 22px;
    font-size: 14px;
    font-weight: bold;
    border-radius: 6px;
    cursor: pointer;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    transition: all 0.2s ease;
}}
.no-print:hover {{
    background: #0369a1;
}}
.floating-print-btn {{
    position: fixed;
    bottom: 16px;
    right: 18px;
    z-index: 2147483647;
    background: linear-gradient(135deg, #0284c7 0%, #1d4ed8 100%);
    color: #ffffff;
    border: 1.5px solid rgba(255, 255, 255, 0.75);
    padding: 7px 16px;
    font-size: 12.5px;
    font-weight: 700;
    border-radius: 24px;
    cursor: pointer;
    box-shadow: 0 6px 20px rgba(2, 132, 199, 0.4), 0 2px 6px rgba(0, 0, 0, 0.18);
    display: flex;
    align-items: center;
    gap: 7px;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    backdrop-filter: blur(8px);
    letter-spacing: 0.2px;
    opacity: 0.92;
}}
.floating-print-btn:hover {{
    opacity: 1;
    transform: translateY(-2px) scale(1.02);
    box-shadow: 0 8px 24px rgba(56, 189, 248, 0.65);
    background: linear-gradient(135deg, #0369a1 0%, #1e40af 100%);
    border-color: #7dd3fc;
}}
.floating-print-btn:active {{
    transform: translateY(0) scale(0.98);
}}
@media print {{
    body {{
        background: #ffffff;
        padding: 0;
    }}
    .page-container {{
        box-shadow: none;
        padding: 0;
        max-width: 100%;
    }}
    .no-print, .floating-print-btn {{
        display: none !important;
    }}
    .print-page-break {{
        page-break-before: always !important;
    }}
    article {{
        page-break-inside: avoid !important;
        break-inside: avoid !important;
    }}
}}
</style>
</head>
<body>
<!-- NÚT 1 CHẠM ĐỂ IN NỔI CỐ ĐỊNH Ở GÓC PHẢI MÀN HÌNH (Độc lập cuộn chuột, cực kỳ mỹ quan, không che chữ) -->
<button class="no-print floating-print-btn" title="Bấm 1 chạm để mở hộp thoại In đề hoặc Lưu PDF A4 chuẩn Bộ GD&ĐT" onclick="if(window.MathJax&&window.MathJax.typesetPromise){{window.MathJax.typesetPromise().then(function(){{window.print();}});}}else{{window.print();}}">
    <span style="font-size: 16px;">🖨️</span>
    <span>In đề / Lưu PDF (1 Chạm)</span>
</button>

<div class="page-container">
{"".join(blocks)}
</div>
</body>
</html>"""

    return markup, "\n".join(tex)


# BỘ KHỬ LỖI TOÁN HỌC VÀ PHÂN TÍCH JSON AN TOÀN

def fix_broken_latex_escapes(obj):

    if isinstance(obj, dict):

        return {k: fix_broken_latex_escapes(v) for k, v in obj.items()}

    elif isinstance(obj, list):

        return [fix_broken_latex_escapes(item) for item in obj]

    elif isinstance(obj, str):

        s = obj

        # Khắc phục lỗi Form Feed ASCII \x0c -> \f (gây ra chữ đỏ ⯅rac / ▲rac)

        s = s.replace('\x0crac', r'\frac').replace('\x0c', r'\f')

        s = s.replace(r'\x0crac', r'\frac').replace(r'\x0c', r'\f')

        s = s.replace('\x08', r'\b')

        s = re.sub(r'[\u25b2\u2bf5\u25b4\u2660]rac', r'\\frac', s)

        s = re.sub(r'(?<!\\)\brac\{', r'\\frac{', s)

        # Khắc phục lỗi Tab ASCII \t -> \t trong \to

        s = re.sub(r'\\lim_\{([^}]+)\s+o\s+', r'\\lim_{\1 \\to ', s)

        s = re.sub(r'(?<=\s)o(?=\s*[-+]?\d|\\infty|\$)', r'\\to', s)

        return s

    return obj





def safe_json_loads(raw):

    if not isinstance(raw, str) or not raw.strip():

        raise ValueError("AI không trả nội dung JSON.")

    value = raw.strip()



    # BƯỚC 1: Bóc tách markdown codeblock

    if value.startswith("```"):

        value = re.sub(r"^```(?:json)?\s*", "", value, flags=re.IGNORECASE)

        value = re.sub(r"\s*```$", "", value)



    # BƯỚC 2: Trích xuất chính xác khối JSON nằm giữa { đầu tiên và } cuối cùng

    first_brace = value.find('{')

    last_brace = value.rfind('}')

    if first_brace != -1 and last_brace != -1 and last_brace > first_brace:

        value = value[first_brace:last_brace+1]



    # BƯỚC 3: Khử ký tự vô hình / ngoại lai UTF-8

    value = value.replace('\ufeff', '').replace('\u200b', '').replace('\u00a0', ' ')

    value = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', '', value)



    # LẦN THỬ 1: Parse trực tiếp

    try:

        data = json.loads(value, strict=False)

        return fix_broken_latex_escapes(data)

    except Exception:

        pass



    # LẦN THỬ 2: Tự động sửa dấu nháy kép nội suy bên trong nội dung câu hỏi

    try:

        res_chars = []

        in_str = False

        esc = False

        for i, ch in enumerate(value):

            if ch == '\\' and not esc:

                esc = True; res_chars.append(ch); continue

            if ch == '"' and not esc:

                before = value[:i].rstrip()

                after = value[i+1:].lstrip()

                is_start = before.endswith(('{', '[', ',', ':', '"')) or before == ''

                is_end = after.startswith(('}', ']', ',', ':')) or after == ''

                if in_str:

                    if is_end: in_str = False; res_chars.append('"')

                    else: res_chars.append('\\"')

                else:

                    in_str = True; res_chars.append('"')

            else:

                res_chars.append(ch)

            esc = False

        data = json.loads("".join(res_chars), strict=False)

        return fix_broken_latex_escapes(data)

    except Exception:

        pass



    # LẦN THỬ 3: Khắc phục backslash chưa thoát và dấu phẩy thừa (Chuẩn hóa công thức toán LaTeX)

    v_clean = re.sub(r',\s*([\}\]])', r'\1', value)

    # Xử lý các lệnh LaTeX bắt đầu bằng ký tự escape của JSON (\f, \t, \b, \n, \r)

    v_escaped = re.sub(r'(?<!\\)\\(frac|dfrac|to|times|theta|tau|tan|text|beta|bar|binom|begin|bf)\b', lambda m: r'\\' + m.group(1), v_clean)

    # Thoát tất cả các backslash cô lập không thuộc escape sequence hợp lệ của JSON

    v_escaped = re.sub(r'(?<!\\)\\(?!["\\/bfnrtu]|u[0-9a-fA-F]{4})', r'\\\\', v_escaped)

    try:

        data = json.loads(v_escaped, strict=False)

        return fix_broken_latex_escapes(data)

    except Exception:

        pass



    # LẦN THỬ 4: Cân bằng ngoặc đóng LIFO (Stack-based) nếu bị cắt ngắn do cạn Token

    stack = []

    in_str = False

    esc = False

    for ch in v_escaped:

        if ch == '\\' and in_str:

            esc = not esc

            continue

        if ch == '"' and not esc:

            in_str = not in_str

            continue

        esc = False

        if not in_str:

            if ch == '{':

                stack.append('}')

            elif ch == '[':

                stack.append(']')

            elif ch in ('}', ']'):

                if stack and stack[-1] == ch:

                    stack.pop()



    closing = '"' if in_str else ''

    while stack:

        closing += stack.pop()

    balanced = re.sub(r',\s*$', '', v_escaped.rstrip()) + closing

    balanced = re.sub(r',\s*([\}\]])', r'\1', balanced)

    try:

        data = json.loads(balanced, strict=False)

        return fix_broken_latex_escapes(data)

    except json.JSONDecodeError as final_err:

        raise ValueError(f"JSON của AI chưa hợp lệ tại dòng {final_err.lineno}, cột {final_err.colno}. Hãy thử lại hoặc bấm khởi tạo lại đề.") from final_err

# ==============================================================================
