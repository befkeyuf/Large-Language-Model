# 基因序列分析工具
import sys

def analyze_gene_sequence(sequence):
    nucleotide_counts = {
        'A': sequence.count('A'),
        'C': sequence.count('C'),
        'G': sequence.count('G'),
        'T': sequence.count('T')
    }
    gc_content = (nucleotide_counts['G'] + nucleotide_counts['C']) / len(sequence)
    
    report = f"序列长度: {len(sequence)}
"
    report += "核苷酸频率:
"
    for nt, count in nucleotide_counts.items():
        report += f"{nt}: {count} ({count/len(sequence):.2%})
"
    report += f"GC含量: {gc_content:.2%}
"
    
    if gc_content > 0.6:
        report += "预测结果: 高GC含量区域，可能为编码区"
    elif gc_content < 0.4:
        report += "预测结果: 低GC含量区域，可能为非编码区"
    else:
        report += "预测结果: 中等GC含量，需要进一步分析"
    
    return report

if __name__ == "__main__":
    input_sequence = input("请输入DNA序列: ") or "ATCGTAGCTAGCTACGT"
    result = analyze_gene_sequence(input_sequence)
    
    output_file = "gene_analysis_report.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(result)
    
    print(f"分析完成，结果已保存至 {output_file}")
    print("示例使用方法: python gene_analysis.py")