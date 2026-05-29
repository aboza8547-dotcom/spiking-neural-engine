# 🧠 Advanced Spiking Neural Engine

A lightweight, modular Python engine built completely from scratch. This engine combines **complex number operations** with a biologically-inspired **Spiking Neural Network (SNN)** featuring online learning via **Spike-Timing-Dependent Plasticity (STDP)** and computational **convergence tracking**.

محرك برمجبي خفيف الوزن ومقسّم إلى ملفات، مبني بالكامل من الصفر بلغة بايثون. يدمج هذا المحرك بين **عمليات الأعداد المركبة** ونموذج **الشبكات العصبية النبضية (SNN)** المستوحاة حيوياً، وتتميز بالتعلم المباشر عبر **اللدونة المعتمدة على توقيت النبضات (STDP)** ومراقبة **استقرار الحسابات**.

---

## 📁 Project Structure (هيكل المشروع)

The codebase is organized into clean, single-responsibility files:
تم تنظيم الأكواد في ملفات منفصلة تؤدي كل منها وظيفة محددة:

* `fractional_cell.py`: Custom wrapper for highly precise float arithmetic.
* `complex_cell.py`: Full complex number mathematics (real & imaginary coordinates).
* `spiking_cell.py`: The spiking neuron core (potential, thresholds, firing, and STDP rules).
* `convergence_cell.py`: Utility to monitor value stability in iterative algorithms.
* `network.py`: The network simulation container managing step-propagation and training loops.
* `main.py`: Main execution environment and validation script.

---

## ✨ Features (المميزات الهندسية للنموذج)

1. **Event-Driven Energy Efficiency (كفاءة الطاقة المعتمدة على الأحداث):** Neurons remain idle and consume zero computational overhead unless their internal membrane potential overcomes the firing threshold.
   الخلايا العصبية تظل خامدة ولا تستهلك أي مجهود حوسبي إلا إذا تخطى جهدها الداخلي عتبة الإطلاق المحددة.

2. **Self-Governing Online Learning (التعلم الذاتي الفوري):** Utilizes the biological STDP rule inside `SpikingCell`. Causal firing strengthens connections, while anti-causal firing weakens them—without backpropagation or global labels.
   يستخدم قاعدة STDP الحيوية لتحديث الأوزان؛ إطلاق النبضات السببي يقوي الروابط، بينما الإطلاق العكسي يضعفها، دون الحاجة للانتشار الخلفي التقليدي.

3. **Phase & Magnitude Representation (تمثيل القيمة والاتجاه):** The `ComplexCell` enables the architecture to represent multidimensional features like frequency, phase, or physical orientation natively.
   تسمح الأعداد المركبة للخلية بالتعبير عن سمات متعددة الأبعاد كالتردد، الطور، أو الاتجاه الفيزيائي في آنٍ واحد.

---

## 🚀 Getting Started (بدء التشغيل)

### Prerequisites (المتطلبات)
* **Python >= 3.8**
* **Zero External Dependencies:** Built entirely with Python's standard library (`math`, `dataclasses`).
* **بدون مكتبات خارجية:** يعتمد بالكامل على مكتبة بايثون القياسية.

### Execution (التشغيل)
Run the complete engine simulation via the terminal:
شغّل المحرك بالكامل من خلال الـ Terminal عبر الأمر التالي:

```bash
python main.py