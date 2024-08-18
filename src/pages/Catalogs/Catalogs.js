/* eslint-disable */
import {
  Button,
  Checkbox,
  Divider,
  Form,
  Input,
  Layout,
  Modal,
  Select,
  Switch,
  Table,
  Tag,
  theme,
} from "antd";
import { USERS } from "../../mocks/user-data";
import { Content, Header } from "antd/es/layout/layout";
import { ReloadOutlined, SettingOutlined } from "@ant-design/icons";
import React, { useContext, useRef, useState, useEffect } from "react";
import Statistic from "antd/es/statistic/Statistic";
import Search from "antd/es/input/Search";
import "./Catalogs.css";

function Catalogs() {
  const [dataSource, setDataSource] = useState(USERS);
  const [form] = Form.useForm();
  const [fromValues, setFormValues] = useState();
  const {
    token: { colorBgContainer },
  } = theme.useToken();

  const [filteredInfo, setFilteredInfo] = useState({});
  const handleChange = (pagination, filters) => {
    setFilteredInfo(filters);
  };

  const [isModalOpen, setIsModalOpen] = useState(false);
  const showModal = () => {
    setIsModalOpen(true);
  };

  const handleCancel = () => {
    setIsModalOpen(false);
  };

  const defaultColumns = [
    {
      title: "Имя",
      dataIndex: "name",
      key: "name",
      width: 312,
      sorter: (a, b) => a.name.length - b.name.length,
      render: (text) => <a>{text}</a>,
    },
    {
      title: "Должность",
      dataIndex: "job",
      key: "job",
      width: 145,
      filters: [
        {
          text: "Front-end",
          value: "Front-end",
        },
        {
          text: "Back-end",
          value: "Back-end",
        },
        {
          text: "Аналитик",
          value: "Аналитик",
        },
        {
          text: "Дизайнер",
          value: "Дизайнер",
        },
      ],
      filteredValue: filteredInfo.job || null,
      onFilter: (value, record) => record.job.includes(value),
    },
    {
      title: "Отдел",
      dataIndex: "section",
      key: "section",
      width: 188,
      filters: [
        {
          text: "Веб-разработка",
          value: "Веб-разработка",
        },
        {
          text: "Мобильная разработка",
          value: "Мобильная разработка",
        },
        {
          text: "Аналитика",
          value: "Аналитика",
        },
        {
          text: "Дизайн",
          value: "Дизайн",
        },
      ],
      filteredValue: filteredInfo.section || null,
      onFilter: (value, record) => record.section.includes(value),
    },
    {
      title: "Статус",
      dataIndex: "status",
      key: "status",
      width: 145,
      editable: true,
      filters: [
        {
          text: "На работе",
          value: "На работе",
        },
        {
          text: "В отпуске",
          value: "В отпуске",
        },
      ],
      filteredValue: filteredInfo.status || null,
      onFilter: (value, record) => record.status.includes(value),
    },
    {
      title: "Тип найма",
      dataIndex: "recruitment",
      key: "recruitment",
      width: 145,
      editable: true,
      filters: [
        {
          text: "Штатный",
          value: "Штатный",
        },
        {
          text: "Аутсорс",
          value: "Аутсорс",
        },
      ],
      filteredValue: filteredInfo.recruitment || null,
      onFilter: (value, record) => record.recruitment.includes(value),
    },
    {
      title: "Навыки",
      dataIndex: "skills",
      key: "skills",
      width: 200,
      render: (_, { skills }) => (
        <>
          {skills.length !== 0 &&
            skills.map((skill) => {
              let color = skill.length > 5 ? "geekblue" : "green";
              if (skill === "volcano") {
                color = "volcano";
              } else if (skill === "red") {
                color = "red";
              } else if (skill === "green") {
                color = "green";
              } else if (skill === "geekblue") {
                color = "geekblue";
              } else if (skill === "gold") {
                color = "gold";
              } else if (skill === "cyan") {
                color = "cyan";
              } else if (skill === "magenta") {
                color = "magenta";
              } else if (skill === "purple") {
                color = "purple";
              }
              return (
                <Tag color={color} key={skill}>
                  {skill.toUpperCase()}
                </Tag>
              );
            })}
        </>
      ),
      filters: [
        {
          text: "green",
          value: "green",
        },
        {
          text: "geekblue",
          value: "geekblue",
        },
        {
          text: "gold",
          value: "gold",
        },
        {
          text: "magenta",
          value: "magenta",
        },
        {
          text: "cyan",
          value: "cyan",
        },
        {
          text: "purple",
          value: "purple",
        },
      ],
      filteredValue: filteredInfo.skills || null,
      onFilter: (value, record) => record.skills.includes(value),
    },
  ];

  // Редактирование строк
  const EditableContext = React.createContext(null);
  const EditableRow = ({ index, ...props }) => {
    const [form] = Form.useForm();
    return (
      <Form form={form} component={false}>
        <EditableContext.Provider value={form}>
          <tr {...props} />
        </EditableContext.Provider>
      </Form>
    );
  };
  const EditableCell = ({
    title,
    editable,
    children,
    dataIndex,
    record,
    handleSave,
    ...restProps
  }) => {
    const [editing, setEditing] = useState(false);
    const inputRef = useRef(null);
    const form = useContext(EditableContext);
    useEffect(() => {
      if (editing) {
        inputRef.current?.focus();
      }
    }, [editing]);
    const toggleEdit = () => {
      setEditing(!editing);
      form.setFieldsValue({
        [dataIndex]: record[dataIndex],
      });
    };
    const save = async () => {
      try {
        const values = await form.validateFields();
        toggleEdit();
        handleSave({
          ...record,
          ...values,
        });
      } catch (errInfo) {
        console.log("Save failed:", errInfo);
      }
    };
    let childNode = children;
    if (editable) {
      childNode = editing ? (
        <Form.Item
          style={{
            margin: 0,
          }}
          name={dataIndex}
          rules={[
            {
              required: true,
              message: `${title} is required.`,
            },
          ]}
        >
          <Input ref={inputRef} onPressEnter={save} onBlur={save} />
        </Form.Item>
      ) : (
        <div
          className="editable-cell-value-wrap"
          style={{
            paddingInlineEnd: 24,
          }}
          onClick={toggleEdit}
        >
          {children}
        </div>
      );
    }
    return <td {...restProps}>{childNode}</td>;
  };

  const [count, setCount] = useState(2);

  const handleAdd = (values) => {
    const newData = {
      key: count,
      name: values.name,
      job: values.job,
      section: values.section,
      status: values.status || 'На работе',
      recruitment: values.recruitment || 'Штатный',
      skills: values.skills || ['gold'],
    };
    setDataSource([...dataSource, newData]);
    setCount(count + 1);
  };

  const handleSave = (row) => {
    const newData = [...dataSource];
    const index = newData.findIndex((item) => row.key === item.key);
    const item = newData[index];
    newData.splice(index, 1, {
      ...item,
      ...row,
    });
    setDataSource(newData);
  };

  const components = {
    body: {
      row: EditableRow,
      cell: EditableCell,
    },
  };

  const columns = defaultColumns.map((col) => {
    if (!col.editable) {
      return col;
    }
    return {
      ...col,
      onCell: (record) => ({
        record,
        editable: col.editable,
        dataIndex: col.dataIndex,
        title: col.title,
        handleSave,
      }),
    };
  });

  const [value, setValue] = useState("");

  const onSearch = (e) => {
    const currValue = e.target.value;
    setValue(currValue);

    const filteredData = USERS.filter((entry) =>
      entry.name.toLowerCase().includes(currValue)
    );
    setDataSource(filteredData);
  };

  const onSubmit = (values) => {
    setFormValues(values);
    setIsModalOpen(false);
    handleAdd(values);
  };

  return (
    <Layout
      style={{
        height: "calc(100vh - 48px)",
      }}
    >
      <Layout>
        <Header
          style={{
            padding: 0,
            background: colorBgContainer,
          }}
        >
          <div className="header__buttons">
            <Statistic title="Каталог" value={USERS.length}></Statistic>
            <Button
              onClick={showModal}
              type="primary"
              style={{
                marginBottom: 16,
              }}
            >
              + Добавить сотрудника
            </Button>
            <Modal
              title="Добавить сотрудника"
              centered
              open={isModalOpen}
              okText="Добавить"
              okButtonProps={{
                htmlType: "submit",
              }}
              onCancel={handleCancel}
              modalRender={(dom) => (
                <Form
                  layout="vertical"
                  form={form}
                  name="form_in_modal"
                  initialValues={{
                    modifier: "public",
                  }}
                  clearOnDestroy
                  onFinish={(values) => onSubmit(values)}
                >
                  {dom}
                </Form>
              )}
            >
              <Divider></Divider>
              <Form.Item label="ФИО" name="name" layout="vertical">
                <Input placeholder="Константинопольский Константин Константинович"></Input>
              </Form.Item>
              <Form.Item label="Почта" name="email" layout="vertical">
                <Input placeholder="example@gmail.com"></Input>
              </Form.Item>
              <Form.Item name="section" label="Отдел">
                <Select
                  showSearch
                  placeholder="Введите название или выберите из списка"
                >
                  <Option value="Веб-разработка">Веб-разработка</Option>
                  <Option value="Мобильная разработка">
                    Мобильная разработка
                  </Option>
                  <Option value="Аналитика">Аналитика</Option>
                  <Option value="Дизайн">Дизайн</Option>
                </Select>
              </Form.Item>
              <Form.Item name="job" label="Должность">
                <Select
                  showSearch
                  placeholder="Введите название или выберите из списка"
                >
                  <Option value="Front-end">Front-end</Option>
                  <Option value="Back-end">Back-end</Option>
                  <Option value="Аналитик">Аналитик</Option>
                  <Option value="Дизайнер">Дизайнер</Option>
                </Select>
              </Form.Item>
              <Form.Item name="invite" valuePropName="checked">
                <Checkbox>Пригласить сотрудника в ГазпромID</Checkbox>
              </Form.Item>
              <Divider></Divider>
            </Modal>
          </div>
        </Header>
        <div className="filters">
          <Search
            style={{
              width: "315px",
              borderRadius: 0,
            }}
            value={value}
            onChange={onSearch}
          ></Search>
          <div className="buttons">
            Отображать уволенных: <Switch></Switch>
            <Button icon={<ReloadOutlined />}></Button>
            <Button icon={<SettingOutlined />}></Button>
          </div>
        </div>
        <Content
          style={{
            margin: "0 16px 0",
          }}
        >
          <Table
            columns={columns}
            components={components}
            dataSource={dataSource}
            onChange={handleChange}
            rowClassName={() => "editable-row"}
            style={{
              padding: 24,
              minHeight: 360,
              background: colorBgContainer,
            }}
          ></Table>
        </Content>
      </Layout>
    </Layout>
  );
}

export default Catalogs;
