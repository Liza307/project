import {
  Avatar,
  Badge,
  Breadcrumb,
  Button,
  Card,
  ConfigProvider,
  Flex,
  Input,
  Layout,
  Tag,
  theme,
  Tooltip,
} from "antd";
import "./Projects.css";
import { Link } from "react-router-dom";
import { UsergroupAddOutlined } from "@ant-design/icons";
import Text from "antd/lib/typography/Text";
import { PROJECTS } from "../../mocks/user-data";
import { Header } from "antd/es/layout/layout";
import { useState } from "react";

function Projects() {
  const [dataSource, setDataSource] = useState(PROJECTS);
  const [count, setCount] = useState(2);
  const [value, setValue] = useState("");
  const { Search } = Input;

  const {
    token: { colorBgContainer },
  } = theme.useToken();

  const onSearch = (e) => {
    const currValue = e.target.value;
    setValue(currValue);

    const filteredData = PROJECTS.filter((entry) =>
      entry.title.toLowerCase().includes(currValue)
    );
    setDataSource(filteredData);
  };

  const handleAddProject = (values) => {
    const newData = {
      key: count,
      title: values.title || "Название проекта",
      description: values.description || "Краткое описание проекта ",
      project_value: values.project_value || 0,
      worker_value: values.worker_value,
      recruitment: values.recruitment || "Штатный",
      tags: values.tags || [],
      avatars: values.avatars || [],
    };
    setDataSource([...dataSource, newData]);
    setCount(count + 1);
  };

  return (
    <ConfigProvider
      theme={{
        components: {
          Card: {
            headerFontSize: 16,
          },
        },
      }}
    >
      <Layout
        style={{
          height: "calc(100vh - 48px)",
        }}
      >
        <Header
          style={{
            padding: "16px 24px",
            background: colorBgContainer,
            display: "flex",
            flexDirection: "column",
            height: 154,
          }}
        >
          <Breadcrumb items={[{ title: "Проекты" }]}></Breadcrumb>
          <Text
            style={{
              fontSize: 20,
              fontWeight: 500,
              lineHeight: "28px",
            }}
          >
            Проекты
          </Text>
          <div
            style={{
              display: "flex",
              flexDirection: "row",
              justifyContent: "space-between",
            }}
          >
            <div
              style={{
                width: 520,
                display: "flex",
              }}
            >
              <Search
                style={{
                  width: 520,
                  borderRadius: 0,
                }}
                value={value}
                onChange={onSearch}
                allowClear
                enterButton="Поиск"
              ></Search>
            </div>
            <Button
              onClick={handleAddProject}
              type="primary"
              style={{
                backgroundColor: "#fff",
                color: "#000",
                border: "1px solid #D9D9D9",
                boxShadow: "none",
                borderRadius: 0,
              }}
            >
              + Добавить проект
            </Button>
          </div>
        </Header>
        <Flex
          gap="middle"
          style={{
            margin: "24px",
            flexWrap: "wrap",
            overflowY: "auto",
          }}
        >
          {dataSource.map((project) => (
            <Card
              title={project.title}
              size="small"
              className="card__title"
              style={{
                width: 320,
                height: 212,
                borderRadius: 0,
                overflow: "hidden",
              }}
            >
              <div className="card__data">
                <Text
                  style={{ textOverflow: "ellipsis", maxWidth: "288px" }}
                  className="card__more"
                >
                  {project.description}
                </Text>
                <Flex
                  gap="12px 0"
                  wrap
                  style={{
                    margin: "12px 0 4px",
                  }}
                >
                  {project.tags.length > 0 ? (
                    project.tags.map((text) => {
                      let color = "";
                      if (text.name === "Высокий") {
                        color = "purple";
                      } else if (text.name === "Выполнено") {
                        color = "green";
                      } else if (text.name === "Аутсорс") {
                        color = "orange";
                      } else if (text.name === "Средний") {
                        color = "volcano";
                      } else if (text.name === "В процессе") {
                        color = "blue";
                      } else if (text.name === "Не начато") {
                        color = "gold";
                      }
                      return <Tag color={color}>{text.name}</Tag>;
                    })
                  ) : (
                    <Button
                      style={{
                        border: "1px dashed #E8E7E7",
                        width: 77,
                        height: 22,
                        borderRadius: 2,
                      }}
                    >
                      + New tag
                    </Button>
                  )}
                </Flex>
                {project.project_value !== 0 ? (
                  <div
                    style={{
                      flexDirection: "row",
                      width: "100%",
                    }}
                    className="card__projects"
                  >
                    <Link
                      style={{
                        color: "#1890FF",
                      }}
                      to={""}
                    >
                      Подчиненные проекты
                    </Link>
                    <Badge
                      className="card__badge"
                      count={project.project_value}
                      style={{
                        backgroundColor: "#FFF",
                        color: "#1890FF",
                        fontWeight: "500",
                        fontSize: "14px",
                        lineHeight: "24px",
                      }}
                    ></Badge>
                  </div>
                ) : (
                  <div
                    style={{
                      flexDirection: "row",
                      width: "100%",
                    }}
                    className="card__projects"
                  >
                    <Link
                      style={{
                        color: "#1890FF",
                        height: 22,
                      }}
                      to={""}
                    ></Link>
                    <Badge
                      className="card__badge"
                      count={project.project_value}
                      style={{
                        backgroundColor: "#FFF",
                        color: "#1890FF",
                        fontWeight: "500",
                        fontSize: "14px",
                        lineHeight: "24px",
                      }}
                    ></Badge>
                  </div>
                )}
                <div
                  style={{
                    margin: "6px 0 4px",
                  }}
                >
                  <Text
                    style={{
                      fontSize: "14px",
                      fontWeight: "500",
                      marginRight: "5px",
                    }}
                  >
                    Сотрудники
                  </Text>
                  <Text
                    style={{
                      fontSize: "14px",
                      fontWeight: "500",
                    }}
                  >
                    {project.worker_value}
                  </Text>
                </div>
                <Avatar.Group
                  size="large"
                  max={{
                    count: 4,
                    style: {
                      color: "#f56a00",
                      backgroundColor: "#fde3cf",
                      cursor: "pointer",
                    },
                    popover: {
                      trigger: "click",
                    },
                  }}
                >
                  {project.avatars.length > 0 ? (
                    project.avatars.map((avatar) => (
                      <Tooltip title={avatar.name} placement="top">
                        <Avatar
                          style={{
                            backgroundColor: avatar.color,
                          }}
                          src={avatar.image}
                        />
                      </Tooltip>
                    ))
                  ) : (
                    <Button
                      icon={<UsergroupAddOutlined></UsergroupAddOutlined>}
                      style={{
                        border: "1px dashed #E8E7E7",
                        borderRadius: "50%",
                        width: 40,
                        height: 40,
                      }}
                    ></Button>
                  )}
                </Avatar.Group>
              </div>
            </Card>
          ))}
        </Flex>
      </Layout>
    </ConfigProvider>
  );
}

export default Projects;
