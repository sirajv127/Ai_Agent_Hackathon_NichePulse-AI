import React from 'react';
import ReactMarkdown from 'react-markdown';
import jsPDF from 'jspdf';
import html2canvas from 'html2canvas';
import './ReportCard.css';

const ReportCard = ({ report, onDelete }) => {
  const reportContentId = `report-content-${report.id}`;

  const handleDownloadPdf = () => {
    const input = document.getElementById(reportContentId);
    html2canvas(input).then((canvas) => {
      const imgData = canvas.toDataURL('image/png');
      const pdf = new jsPDF('p', 'px', 'a4');
      const pdfWidth = pdf.internal.pageSize.getWidth();
      const pdfHeight = (canvas.height * pdfWidth) / canvas.width;
      pdf.addImage(imgData, 'PNG', 0, 0, pdfWidth, pdfHeight);
      pdf.save(`report_${report.id}.pdf`);
    });
  };

  const handleDownloadDoc = () => {
    const reportHtml = document.getElementById(reportContentId).innerHTML;
    const header = "<html xmlns:o='urn:schemas-microsoft-com:office:office' "+
        "xmlns:w='urn:schemas-microsoft-com:office:word' "+
        "xmlns='http://www.w3.org/TR/REC-html40'>"+
        "<head><meta charset='utf-8'><title>Export HTML to Word Document</title></head><body>";
    const footer = "</body></html>";
    const sourceHTML = header + reportHtml + footer;

    const source = 'data:application/vnd.ms-word;charset=utf-8,' + encodeURIComponent(sourceHTML);
    const fileDownload = document.createElement("a");
    document.body.appendChild(fileDownload);
    fileDownload.href = source;
    fileDownload.download = `report_${report.id}.doc`;
    fileDownload.click();
    document.body.removeChild(fileDownload);
  };

  return (
    <div className="report-card">
      <div id={reportContentId}>
        <div className="report-card-header">
          <h3>Trend Brief</h3>
          <span className="date-range">{report.date_range}</span>
        </div>
        <div className="report-card-body">
          <ReactMarkdown>{report.generated_brief}</ReactMarkdown>
        </div>
      </div>
      <div className="report-card-footer">
        <button className="download-button doc" onClick={handleDownloadDoc}>
          Download DOC
        </button>
        <button className="download-button pdf" onClick={handleDownloadPdf}>
          Download PDF
        </button>
        <button className="delete-button" onClick={() => onDelete(report.id)}>
          Delete Report
        </button>
      </div>
    </div>
  );
};

export default ReportCard;