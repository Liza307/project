import { Avatar, Card, Flex, Tooltip } from "antd";
import { AntDesignOutlined, UserOutlined } from "@ant-design/icons";
import Text from "antd/lib/typography/Text";
import { Link } from "react-router-dom";

export const nodeTemplate = (node) => {
  if (node.type === "person") {
    return (
      <Card
        title={node.data.department}
        size="small"
        className="card__title"
        style={{
          width: 320,
          borderRadius: 0,
          textAlign: "left",
        }}
      >
        <div className="card__data">
          <div className="card__user-info">
            <img
              className="card__image"
              src={node.data.image}
              alt={node.data.name}
            ></img>
            <div className="card__user-block">
              <Link
                style={{
                  color: "#1890FF",
                }}
                className="card__name"
                to="/profile"
              >
                {node.data.name}
              </Link>
              <Text
                className="card__title"
                style={{
                  opacity: ".45",
                }}
              >
                {node.data.title}
              </Text>
            </div>
          </div>
          <Flex
            gap="12px 0"
            wrap
            style={{
              margin: "12px 0 4px",
            }}
          ></Flex>

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
              {node.data.worker_value}
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
            <Avatar src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png" />
            <Avatar
              style={{
                backgroundColor: "#f56a00",
              }}
            >
              K
            </Avatar>
            <Tooltip title="Ant User" placement="top">
              <Avatar
                style={{
                  backgroundColor: "#87d068",
                }}
                icon={<UserOutlined />}
              />
            </Tooltip>
            <Avatar
              style={{
                backgroundColor: "#1677ff",
              }}
              icon={<AntDesignOutlined />}
            />
            <Avatar
              style={{
                backgroundColor: "#1677ff",
              }}
              icon={<AntDesignOutlined />}
            />
          </Avatar.Group>
        </div>
        {node.data.projects.length !== 0 && (
          <div
            style={{
              alignItems: "flex-start",
            }}
            className="card__projects"
          >
            <div>
              <Text
                style={{
                  fontSize: "14px",
                  fontWeight: "500",
                  marginRight: "5px",
                }}
                to={""}
              >
                Проекты
              </Text>
              <Text
                style={{
                  fontSize: "14px",
                  fontWeight: "500",
                  marginRight: "5px",
                }}
                to={""}
              >
                {node.data.project_value}
              </Text>
            </div>
            <div
              style={{
                marginBottom: 6,
                display: "flex",
                flexDirection: "column",
              }}
              lassName="card__links"
            >
              {node.data.projects.map((project) => (
                <Link
                  to="/projects"
                  className="card__link"
                  style={{
                    alignSelf: "flex-start",
                    color: "#1890FF",
                  }}
                >
                  {project.name}
                </Link>
              ))}
            </div>
            <Link
              to="/projects"
              className="card__link"
              style={{
                fontWeight: "400",
                fontSize: "12px",
                lineHeight: "20px",
                color: "#1890FF",
              }}
            >
              Все проекты
            </Link>
          </div>
        )}
      </Card>
    );
  }

  return node.label;
};
