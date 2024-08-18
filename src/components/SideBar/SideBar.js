import { Menu, theme } from "antd";
import { useLocation, useNavigate } from "react-router-dom";
import { TableOutlined, FormOutlined, UserOutlined } from "@ant-design/icons";
import Sider from "antd/es/layout/Sider";
import "./SideBar.css";

function SideBar() {
  const location = useLocation();
  const navigate = useNavigate();

  const {
    token: { colorBgContainer },
  } = theme.useToken();

  const onClick = (e) => {
    navigate(e.key, {
      replace: true,
    });
  };

  const items = [
    {
      key: "/company",
      icon: <TableOutlined />,
      label: "Компания",
    },
    {
      key: "/projects",
      icon: <FormOutlined />,
      label: "Проекты",
    },
    {
      key: "/catalogs",
      icon: <UserOutlined />,
      label: "Каталог",
    },
    {
      key: "/profile",
      icon: <UserOutlined />,
      label: "Profile",
    },
  ];

  return (
    <Sider
      breakpoint="lg"
      style={{
        background: colorBgContainer,
        boxShadow: '0px 2px 8px 0px rgba(0, 0, 0, 0.15)',
        borderInlineEnd: '0'
      }}
    >
      <Menu
        theme="light"
        mode="inline"
        selectedKeys={[location.pathname]}
        items={items}
        onClick={onClick}
      />
    </Sider>
  );
}

export default SideBar;
