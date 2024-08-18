import { OrganizationChart } from "primereact/organizationchart";
import "./Company.css";
import { COMPANY } from "../../mocks/user-data";
import { useState } from "react";
import { Layout } from "antd";
import { nodeTemplate } from "../../components/Tree/Tree";

function Company(props) {
  const [selection, setSelection] = useState([]);

  return (
    <Layout
      style={{
        height: "calc(100vh - 48px)",
      }}
    >
      <div className="card overflow-x-auto">
        <OrganizationChart
          value={COMPANY}
          selectionMode="multiple"
          selection={selection}
          onSelectionChange={(e) => setSelection(e.data)}
          nodeTemplate={nodeTemplate}
        />
      </div>
    </Layout>
  );
}

export default Company;
